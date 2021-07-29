import requests
import json

class ZendeskApiCallHelper:

    @staticmethod
    def get_tickets(cursor):
        response2 = requests.get(f"https://zcctest.zendesk.com/api/v2/tickets/count", auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
        if not cursor:
            response = requests.get('https://zcctest.zendesk.com/api/v2/tickets.json?page[size]=25', auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
            print({'tickets':response.json(), 'info':response2.json()})
            #return response.json()
            return {'tickets':response.json(), 'info':response2.json()}
        else:
            response = requests.get(cursor, auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
            return {'tickets':response.json(), 'info':response2.json()}

    @staticmethod
    def get_ticket(id):
        response = requests.get(f"https://zcctest.zendesk.com/api/v2/tickets/{id}", auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
        return response.json()

    @staticmethod
    def get_total_tickets_count():
        response = requests.get(f"https://zcctest.zendesk.com/api/v2/tickets/count", auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
        return response.json()