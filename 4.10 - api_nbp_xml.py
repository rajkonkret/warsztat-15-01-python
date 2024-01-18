import xml.etree.ElementTree as ET
import requests as re

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x0000018FD6816610>
table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

data = root.find(".//EffectiveDate").text
print(f"Data tabeli: {data}")

no = root.find(".//No").text  # Data tabeli: 2024-01-18
print(f"Numer tabeli: {no}")  # Numer tabeli: 013/A/NBP/2024

rates = root.findall(".//Rate")
print(rates)

# <Rate>
#                 <Currency>bat (Tajlandia)</Currency>
#                 <Code>THB</Code>
#                 <Mid>0.1136</Mid>
#             </Rate>

# wyciagnac te pola i wypisac
# waluta kod_waluty kurs
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"Currency {currency}, Code: {code}, Mid: {mid}")
# Currency euro, Code: EUR, Mid: 4.4016
