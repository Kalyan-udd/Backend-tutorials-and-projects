# to test the APIs working 
import requests

def getting_a_response(url):
    response = requests.get(url)
    with open("index.html", "w") as f:
        f.write(response.text)
    return response.text

print(getting_a_response(url="https://www.youtube.com"))
