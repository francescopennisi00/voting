from vote_app import create_app
from config import BaseConfig, ProdConfig
import os

env = os.environ.get("VOTE_ENV", 'dev')
# 'dev' è il valore di default ma il value della variabile VOTE_ENV potrebbe anche essere 'prod'
# le effettive configurazioni di development e production sono da definire  nelle rispettive classi in config.py

config = BaseConfig  # si assume classe BaseConfig = classe DevConfig

if env == 'prod':
    config = ProdConfig

app = create_app(config)

if __name__ == '__main__':
    foo = os.getenv('FOO', 'bar')
    print(foo)  # verra' stampato solo se faccio python app.py, non se faccio flask run
    app.run(host='0.0.0.0', debug=True, threaded=True)

# il comando activate può essere usato senza source (che non esiste su ambiente Windows)
# con il Activate su venv (cercare su stack overflow, activate flask without source)
# si trova su Scrpts (virtual env Python è diverso su Windows che su Linux)
# forse si attiva in automatico
# il feedback se e' attivo lo abbiamo da (venv) nella PowerShell
# se attivo posso usare flask al suo interno, infatti nella directory vote posso usare flask run --debug
