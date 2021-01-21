import requests
from Utilities.Configuration import getConfig
from Utilities.resources import AddResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        # ID = context.Id

        delete_url = getConfig().get('API Testing', 'EndPoint') + AddResources.DeleteBook

        response_delete = requests.post(delete_url, json={'ID': context.book_Id},
                                        headers={'Content-Type': 'application/json'})

        print(response_delete.json())
