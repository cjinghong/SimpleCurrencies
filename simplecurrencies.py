import json
import requests

url = 'https://restcountries.eu/rest/v2'

response = requests.get(url=url)
jsonData = response.json()

countryCurrencies = []

for country in jsonData:
	countryName = country['name']

	currency = country['currencies'][0]
	currencyName = currency['name']
	currencyCode = currency['code']
	currencySymbol = currency['symbol']

	countryCurrencies.append(
		{
			'country': countryName,
			'currencyName': currencyName,
			'currencyCode': currencyCode,
			'currencySymbol': currencySymbol
		}
	)

print(countryCurrencies[0])

with open('currencies.json', 'w') as currenciesFile:
	json.dump(countryCurrencies, currenciesFile)

