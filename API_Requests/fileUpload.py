import requests

file = {'files': open('abc.txt', 'rb')}

response = requests.post('https://httpbin.org/post', files=file)

print(response.text)

print(response.json()['headers']['Content-Type'])

print(response.headers.get('Content-Type'))
