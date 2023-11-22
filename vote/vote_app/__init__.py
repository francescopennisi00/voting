from flask import Flask
import os
from config import BaseConfig


def create_app(config=BaseConfig):
    app = Flask(__name__)

    app.config.from_object(config)

    @app.route('/')
    def hello():
        foo = os.getenv('FOO', 'bar')
        # bar è il valore di default (nel caso in cui la variabile di ambiente FOO non sia definita)
        return "Hello World! " + str(foo)

    # dimostro che c'è il live reload attivo (attivabile con flask run --debug anziche' solo flask run)
    # il reload permette di fare debug interattivo senza re-build dell'immagine (es. in ambiente Dockerizzato)
    # in pratica, durante il run se viene modificato e salvato il file, posso richiamare le eventuali altre
    # route aggiunte
    @app.route("/healthz")
    def healthz():
        return "Alive!"

    return app