# __missing__ - metoda wykonywan gdy nie ma w słowniku klucza

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsesitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}
# d_python['name']  # KeyError: 'name'

d1 = DefaultDict()
print(d1['name'])  # default
d1['name'] = "Radek"
print(d1)  # {'name': 'Radek'}

a1 = AutoKeyDict()
print(a1)
print(a1['imie'])
print(a1)  # {'imie': 0}

d2 = CaseInsesitiveDict()
d2['name'] = "Radek"
print(d2['NamE'])  # Radek
