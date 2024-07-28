import requests

sc = requests.Session()

sc.auth = ('email', 'key')

sc.headers.update({'Content-Type': 'application/json'})

body = {
    "body": "This is a comment regarding the quality of the response."
}

response = sc.post('https://riteshautomation.atlassian.net/rest/api/2/issue/BAN-34/comment', json=body)
