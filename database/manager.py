import json
import threading
from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'localdb',
        'user': 'root',
        'password': '',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)



