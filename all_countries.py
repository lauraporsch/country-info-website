import requests

restcountries_endpoint = f"https://restcountries.com/v3.1/all"


response = requests.get(url=restcountries_endpoint)
response.raise_for_status()
country_data = response.json()

countries = []

for index in range(len(country_data)):
    country = country_data[index]["name"]["common"]
    countries.append(country)

print(len(countries))
print(countries)