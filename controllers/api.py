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
    )


def get_city_all():
    return Thread(target=(lambda: city.all().to_json())).start()


# Country info calls
def get_countryinfo(name: str):
    return NotImplementedError


def get_countryinfo_all():
    return NotImplementedError


# Country language calls
def get_countrylanguage(name: str):
    return NotImplementedError


def get_countrylanguage_all():
    return NotImplementedError



