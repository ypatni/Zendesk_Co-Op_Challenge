from api import ZendeskApiCallHelper
import json


def get_tickets(event, context):
    try:
        print(event)
        print(event['body'])
        print(type(event['body']))
        cursor = json.loads(event['body'])['cursor']
        tickets = ZendeskApiCallHelper.get_tickets(cursor)
        print(tickets)
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            "body": json.dumps(tickets)
        }

        return response
    except Exception as error:
        print(error)
        return {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            "body": json.dumps(str(error))
        }

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


def main():
    input_event = json.jumps({
            'body': {
    "cursor": "https://zcctest.zendesk.com/api/v2/tickets.json?page%5Bafter%5D=eyJvIjoibmljZV9pZCIsInYiOiJhUmtBQUFBQUFBQUEifQ%3D%3D&page%5Bsize%5D=25"
}
        },{})
    get_tickets(
        input_event
    )

if __name__ == "__main__":
    main()