import requests

body = {
    "fields": {
        "project":
            {
                "key": "BAN"
            },
        "summary": "REST ye merry gentlemen.",
        "description": "Creating of an issue using project keys and issue type names using the REST API",
        "issuetype": {
            "name": "Bug"
        }
    }
}

response = requests.post('https://riteshautomation.atlassian.net/rest/api/2/issue',
                         auth=('email', 'apikey')

                         , headers={'Content-Type': 'application/json'},

                         json=body)


print(response.json())
print(response.status_code)
