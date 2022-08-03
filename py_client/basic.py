import requests

endpoint = "https://httpbin.org/"
endpoint = "https://princetongrade.com/"
# endpoint = "https://httpbin.org/something"

get_response = requests.get(endpoint)
print(get_response.text)

#