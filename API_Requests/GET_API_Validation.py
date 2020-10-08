import json
import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty'}, )

print(response.text)

print(type(response.text))

dict_response = json.loads(response.text)

print(type(dict_response))

print(dict_response[0]['book_name'])

json_response = response.json()

print(json_response[0]['book_name'])

print(json_response[1]['isbn'])

status_code = response.status_code

assert status_code == 200

content_type = response.headers['Content-Type']

assert content_type == 'application/json;charset=UTF-8'

for actual_book in json_response:

    if actual_book['isbn'] == 'ASDF':
        break

expected_book = {"book_name": "Learn RestAssured",
                 "isbn": "ASDF",
                 "aisle": "228"}

assert actual_book == expected_book
