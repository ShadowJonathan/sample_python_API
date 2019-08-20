# Python core imports
from threading import Thread
import json as JSON

# Local model imports
from models.city import city
from models.country import country
from models.countryinfo import countryinfo
from models.countrylanguage import countrylanguage


# City calls
def get_city(name: str) -> JSON:
    return Thread(
        target=(
            lambda: city.where('lower(Name) = ?', [name.lower()]).to_json()
        )
    ).start()


def get_city_all():
    return Thread(target=(lambda: city.all().to_json())).start()


def get_country(name: str) -> JSON:
    return Thread(
        target=(
            lambda: country.where('lower(Name) = ?',  [name.lower()]).to_json()
        )
    ).start()


def get_country_all() -> JSON:
    return Thread(target=lambda: city.all().to_json()).start()


# Country info calls
def get_countryinfo(id: str):
    return Thread(
        target=(
            lambda: countryinfo.where('_id = ?',  [id.lower()]).to_json()
        )
    ).start()


# Country language calls
def get_countrylanguage(language: str):
    return Thread(
        target=(
            lambda: countrylanguage.where(
                'lower(Language) = ?',
                [language.lower()]
            ).to_json()
        )
    ).start()


def get_countrylanguage_all():
    return Thread(target=lambda: countrylanguage.all().to_json()).start()
