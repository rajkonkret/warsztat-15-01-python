# stworzyc słownik z funkcją, ktorą zwraca najdłuzszy klucz w słowniku

class LongestKeyDict(dict):

    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


art = LongestKeyDict()
art['tomasz'] = 45
art['abraham'] = 7
art['zen'] = 1
print(art.longest_key())  # abraham
assert 'abraham' == art.longest_key()
# assert 'zen' == art.longest_key(), "Błąd"  # AssertionError: Błąd
art['siedemo'] = 9
print(art.longest_key())  # abraham
