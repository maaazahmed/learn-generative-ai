import requests
from requests import Response



respose:Response = requests.get("http://127.0.0.1:8000/hi/Maaz%20Ahmed")

print(respose.json())