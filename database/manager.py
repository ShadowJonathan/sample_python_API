# Python core imports
import os

# Third-party imports
from orator import DatabaseManager, Model

# Importing local models
from models.city import city
from models.country import country
from models.countryinfo import countryinfo
from models.countrylanguage import countrylanguage


class Database:
    db = None

    City = city
    Country = country
    CountryInfo = countryinfo
    CountryLanguage = countrylanguage

    # Config
    config = {}

    def __init__(self):
        # Set config
        self.config = {
            'mysql': {
                'driver': 'mysql',
                'host': os.getenv('DB_HOST'),
                'database': os.getenv('DB_NAME'),
                'user': os.getenv('DB_USER'),
                'password': os.getenv('DB_PASSWORD'),
                'prefix': ''
            }
        }

        # Create database from config
        self.db = DatabaseManager(self.config)

        # Auto-resolve connection
        Model.set_connection_resolver(self.db)


# Create public instance
db = Database()
