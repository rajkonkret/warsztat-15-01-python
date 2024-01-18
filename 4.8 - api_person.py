import requests as re
from pydantic import BaseModel

url = 'https://randomuser.me/api/'

response = re.get(url)
data = response.json()
print(response.text)
user = data['results'][0]
print(user)
# {'gender': 'male', 'name': {'title': 'Monsieur', 'first': 'Valerio', 'last': 'Gaillard'},
#  'location': {'street': {'number': 6835, 'name': 'Rue Baraban'}, 'city': 'Commugny', 'state': 'St. Gallen',
#               'country': 'Switzerland', 'postcode': 6926,
#               'coordinates': {'latitude': '-55.9325', 'longitude': '-85.1683'},
#               'timezone': {'offset': '+5:00', 'description': 'Ekaterinburg, Islamabad, Karachi, Tashkent'}},
#  'email': 'valerio.gaillard@example.com',
#  'login': {'uuid': 'f5ba63b7-4a35-43e6-804b-f818a38abeb6', 'username': 'crazypanda966', 'password': '5050',
#            'salt': 'sNoto5Bb', 'md5': '0f76750ac0ac45fdb15b2185ffc20bed',
#            'sha1': '7ce61b3e01ef905e9f1cb4af103d968a885ff17d',
#            'sha256': '6e7515727852997a71e2fae194abfaeeb1ed3bf42e59fb42d6be5f1d8f6acf1d'},
#  'dob': {'date': '1974-11-17T22:48:04.009Z', 'age': 49}, 'registered': {'date': '2003-12-14T06:43:48.400Z', 'age': 20},
#  'phone': '076 567 87 46', 'cell': '076 771 21 97', 'id': {'name': 'AVS', 'value': '756.3955.5361.21'},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/54.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/54.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/54.jpg'}, 'nat': 'CH'}
# wypisac imie, nazwisko, email
print(f"Imię: {user['name']['first']}")
print(f"Nazwwisko: {user['name']['last']}")
print(f"Email: {user['email']}")
photo_url = user['picture']['large']
response_photo = re.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)
print("Zdjęcie zapisane")


class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture


user_info = UserInfo(**user)
print(user_info)
print(type(user_info))

response_photo_pydantic = re.get(user_info.picture.large)
with open('user_photo_pydantic.jpg', 'wb') as f:
    f.write(response_photo_pydantic.content)
print("Zdjęcie zapisane")
