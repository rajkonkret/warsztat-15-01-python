import xml.etree.ElementTree as ET
import requests as re
from pydantic import BaseModel
from typing import List


class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRatesTables(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


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
currency_rates = []
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"Currency {currency}, Code: {code}, Mid: {mid}")
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=mid))
# Currency euro, Code: EUR, Mid: 4.4016
exchange_rate_table = ExchangeRatesTables(table=table_name, date=data, number=no, rates=currency_rates)
print(exchange_rate_table.rates[5])
print(exchange_rate_table.rates[9])
