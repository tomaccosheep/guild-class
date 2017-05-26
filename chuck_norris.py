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

json_data = r.json()
