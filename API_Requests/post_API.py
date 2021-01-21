import requests
import json


response = requests.post('https://reqres.in/api/users', json={

        "name": "morpheusl",
        "job": "leader"

}, headers={"Content-Type": "application/json"}, )

print(response.json())

status_code = response.status_code

assert status_code == 201


