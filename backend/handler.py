from api import ZendeskApiCallHelper
import json


def get_tickets(event, context):

    tickets = ZendeskApiCallHelper.get_tickets()

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(tickets)
    }

    return response

def get_ticket(event, context):
    body = {
        "message": "get ticket",
        "input": event
    }

    print(event)

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
    }

    return response