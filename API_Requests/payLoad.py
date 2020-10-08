from Utilities.Configuration import getQuery


def addBody(ISBN):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": ISBN,
        "aisle": "220675",
        "author": "John foed"
    }

    return body


def DBPayLoad(query):
    AddBody = {}

    tp = getQuery(query)

    AddBody['name'] = tp[0]

    AddBody['isbn'] = tp[1]

    AddBody['aisle'] = tp[2]

    AddBody['author'] = tp[3]

    return AddBody
