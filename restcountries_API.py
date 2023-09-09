import requests

COUNTRY = "Belgium"

restcountries_endpoint = f"https://restcountries.com/v3.1/name/{COUNTRY}"


response = requests.get(url=restcountries_endpoint)
response.raise_for_status()
country_data = response.json()
flag = country_data[0]["flags"]["png"]
print(flag)

# common_name = country_data[0]["name"]["common"]
# print(common_name)
# official_name = country_data[0]["name"]["official"]
# print(official_name)
# currency_complete = (country_data[0]["currencies"])
# for currency in currency_complete:
#     print(currency)
#     currency_name = currency_complete[currency]["name"]
#     print(currency_name)
#     currency_symbol = currency_complete[currency]["symbol"]
#     print(currency_symbol)
# capital = country_data[0]["capital"][0]
# print(capital)
# continent = country_data[0]["continents"][0]
# print(continent)
# region = country_data[0]["region"]
# print(region)
# subregion = country_data[0]["subregion"]
# print(subregion)
# languages_complete = country_data[0]["languages"]
# languages = []
# for item in languages_complete:
#     language = languages_complete[item]
#     languages.append(language)
# print(languages)
# coordinates = country_data[0]["latlng"]
# print(coordinates)
# landlocked = country_data[0]["landlocked"]
# print(landlocked)
# maps = country_data[0]["maps"]["googleMaps"]
# print(maps)
# population = country_data[0]["population"]
# print(population)
