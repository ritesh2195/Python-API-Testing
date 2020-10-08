import requests
from behave import given, when, then

from API_Requests.payLoad import addBody
from Utilities.Configuration import getConfig
from Utilities.resources import AddResources


@given(u'The book details added to library')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json'}

    context.url = getConfig()['API Testing']['EndPoint'] + AddResources.AddBook

    context.payLoad = addBody('vghdhlhbh')


@when(u'We execute add book Post method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad,
                                     headers=context.headers
                                     )


@then(u'Book should add successfully')
def step_impl(context):
    response_json = context.response.json()

    print(response_json)

    assert response_json['Msg'] == 'successfully added'
