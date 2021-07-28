import requests
import json

class ZendeskApiCallHelper:
    @staticmethod
    def get_tickets():
        response = requests.get("https://zcctest.zendesk.com/api/v2/tickets.json?page[size]=25", auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
        return response.json()

    @staticmethod
    def get_ticket(id):
        response = requests.get("https://zcctest.zendesk.com/api/v2/tickets", auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma'))
        return response.json()