# search:{{ }}
import requests

# Declare a package with key parameter {{
package = {
    'APPID': '61b3cff64285cad2b26550ab28e58fa8'
}
# }}


# Get parameters and then add them to the dictionary 'package' {{


# Use a while loop to force a choice between city or zip code {{
city_or_zip = 'unset'
while city_or_zip != '1' and city_or_zip != '2':
	city_or_zip = input('1. Search by city\n2. Search by zip code\n:')
# }}

if city_or_zip == '1':
	city = input('What city would you like to know about? ')
	package['q'] = city
if city_or_zip == '2':
	zip_code = input('What zip code would you like to know about? ')
	package['zip'] = zip_code
# }}

# Choose the temperature type through a while loop {{
c_or_f = 'unset'
while c_or_f != '1' and c_or_f != '2':
	c_or_f = input('1. Get temperature in Celcius\n2. Get temperature in Fahrenheit\n: ')
# }}

# Define 'r' as a URL with parameters from 'package' dictionary {{
r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
# }}

json_data = r.json()
print(r.url)

# Print all json data {{
print(json_data)
# }}


# Convert the temperature based on c_or_f, and then output temp and weather {{
if c_or_f == '1':
	temp = int(json_data['main']['temp'] - 273)
elif c_or_f == '2':
	temp = int((json_data['main']['temp'] - 273) * 9/5 + 32)
print('Temperature equals', temp)
print('The weather outside is', json_data['weather'][0]['description'])
# }}
