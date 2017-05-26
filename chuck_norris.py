import requests

# Declare a package with URL parameters {
package = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
# }


# Define 'r' as a URL with parameters above {
r = requests.post('http://jsonplaceholder.typicode.com/posts', params=package)
# }







		package = {
	'APPID' : '61b3cff64285cad2b26550ab28e58fa8'
	'q' : 'London'
}


json_data = r.json()
