import requests as re  # biblioteka to korzystania z metod http

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