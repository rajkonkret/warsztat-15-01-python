# Odczytac dane z tego api
# jsona przerobic na słownik
# wypisac kilka rzeczy z tego słownika
# zdeserializowac json na obiekty
# z obiektow wypisac dowolne dane
from typing import List

import requests as re
from pydantic import BaseModel

url = 'https://restcountries.com/v3.1/name/Poland'

response = re.get(url)
data = response.json()
print(response.text)

print(data)
print(type(data))  # <class 'list'>
print(data[0].keys())
country = data[0]
print(country['name'])
print(country['name']['common'])
print(country['name']['official'])
print("Stolica kraju", country['capital'][0])  # Stolica kraju Warsaw
print(country['population'])  # 37950802


# "nativeName": {
#         "pol": {
#           "official": "Rzeczpospolita Polska",
#           "common": "Polska"
#         }
#       }
class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    nativeName: NativeName


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]
print(country_data)

for country in country_data:
    print(f"{country.name}, {country.capital} {country.name.nativeName.pol.official}")
# common = 'Poland'
# official = 'Republic of Poland'
# nativeName = NativeName(pol=Pol(official='Rzeczpospolita Polska', common='Polska')), ['Warsaw']
# Rzeczpospolita
# Polska
