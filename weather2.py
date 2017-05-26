# {{ }}
import requests

# Declare a package with key parameter {{
package = {
    'APPID': '61b3cff64285cad2b26550ab28e58fa8',
}
# }}


# Get parameters and then add them to the dictionary 'package' {{


# Use a while loop to force a choice between city or zip code {{
city_or_zip = 'unset'
while city_or_zip != '1' and city_or_zip != '2':
	city_or_zip = input('1. Search by city\n2. Search by zip code ')
# }}

if city_or_zip == '1':
	city = input('What city would you like to know about? ')
	package['q'] = city
if city_or_zip == '2':
	zip_code = input('What zip code would you like to know about? ')
	package['zip'] = zip_code
# }}



# Define 'r' as a URL with parameters from 'package' dictionary {{
r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
# }}

json_data = r.json()
print(r.url)
print(json_data)
