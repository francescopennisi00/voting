from flask import Flask
import os
from config import BaseConfig

def create_app(config=BaseConfig):

    app = Flask(__name__)

    app.config.from_object(config)

    @app.route('/')
    def hello():
        foo = os.getenv('FOO','bar')
        #bar è il valore di default (nel caso in cui la variabile di ambiente non sia definita
        return "Hello World! " + str(foo)

    #dimostro che c'è il live reload attivo
    #permette di fare debug interattivo senza re-build dell'immagine (es. in ambiente Dockerizzato)
    @app.route("/healthz")
    def healthz():
        foo = os.getenv('FOO','bar')
        print(foo)
        return "Alive !"

    return app