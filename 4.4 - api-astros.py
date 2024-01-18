from typing import List

import requests as re  # biblioteka to korzystania z metod http
from pydantic import BaseModel

# pip install requests


url = 'http://api.open-notify.org/astros.json'
# {
#   "message": "success",
#   "number": NUMBER_OF_PEOPLE_IN_SPACE,
#   "people": [
#     {"name": NAME, "craft": SPACECRAFT_NAME},
#   ]
# }
response = re.get(url)
print(response)  # <Response [200]>
# 200 ok
# Rodzaje kodów odpowiedzi HTTP
# HTTP 1xx – Informacyjne kody HTTP
# HTTP 2xx – Kody odpowiedzi HTTP dla sukcesu
# HTTP 3xx – Kody odpowiedzi HTTP dla przekierowania
# HTTP 4xx – Kody odpowiedzi HTTP dla błędów klienta
# HTTP 5xx – Kody odpowiedzi HTTP dla błędów serwera
# Najczęstsze kody odpowiedzi serwera
# HTTP 200 – OK (wszystko działa)
# HTTP 301 – Przekierowanie trwałe (Permanent redirect)
# HTTP 404 – Nie znaleziono (Page not found)
# HTTP 400 Bad Request - przekzalismy błedne parametry
# HTTP 500 – Wewnętrzny błąd serwera (Internal Server Error)
print(response.text)
response_data = response.json()

for i in response_data:  # wypisze klucze słownika
    print(i)
# message
# people
# number
print(response_data['message'])
print(response_data['people'])
print(response_data['number'])

for p in response_data['people']:
    print(p)


# {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
# {'name': 'Andreas Mogensen', 'craft': 'ISS'}
# {'name': 'Satoshi Furukawa', 'craft': 'ISS'}
# {'name': 'Konstantin Borisov', 'craft': 'ISS'}
# {'name': 'Oleg Kononenko', 'craft': 'ISS'}
# {'name': 'Nikolai Chub', 'craft': 'ISS'}
# {'name': "Loral O'Hara", 'craft': 'ISS'}

class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int
    # number: str  #  Input should be a valid string [type=string_type, input_value=7, input_type=int]
    # typy są walidowane prze bibliotek Pydantic


data = AstroData(**response.json())
print(data)
# message = 'success'
# people = [Astronaut(name='Jasmin Moghbeli', craft='ISS'), Astronaut(name='Andreas Mogensen', craft='ISS'),
#           Astronaut(name='Satoshi Furukawa', craft='ISS'), Astronaut(name='Konstantin Borisov', craft='ISS'),
#           Astronaut(name='Oleg Kononenko', craft='ISS'), Astronaut(name='Nikolai Chub', craft='ISS'),
#           Astronaut(name="Loral O'Hara", craft='ISS')]
# number = 7
print(type(data))
print(data.people)

for astronaut in data.people:
    print(f"{astronaut.name}, {astronaut.craft}")
