import requests


author_name ="shakespeare"

url = "https://poetrydb.org/"
url+=author_name
print(url)



response = requests.request("GET", url)

print(response.text)