import requests

# Get parameters {
city = input('What city would you like to know about? ')
# }

# Declare a package with URL parameters {
package = {
    'APPID': '61b3cff64285cad2b26550ab28e58fa8',
    'q': city,
}
# }


# Define 'r' as a URL with parameters above {
r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
# }

json_data = r.json()
print(r.url)
print(json_data)
