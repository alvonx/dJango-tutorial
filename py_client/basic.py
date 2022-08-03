import requests

# endpoint = "https://httpbin.org/"
# endpoint = "https://princetongrade.com/"
# endpoint = "https://httpbin.org/something"
endpoint = 'http:localhost:8000/api/query'
get_response = requests.get(endpoint, json={"name": "deepak"})
print(get_response.text)