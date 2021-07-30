import requests

class ZendeskApiCallHelper:
    @staticmethod
    def get_total_tickets_count():
        """Method to call API to get total number of tickets"""
        return ZendeskApiCallHelper._get_api_call(f"https://zcctest.zendesk.com/api/v2/tickets/count")

    @staticmethod
    def get_tickets(cursor_link):
        """Method to get tickets for a page in increments of 25. Uses a next page link to identify page."""
        count_response = ZendeskApiCallHelper.get_total_tickets_count()

        if not cursor_link:
            cursor_link = 'https://zcctest.zendesk.com/api/v2/tickets.json?page[size]=25'

        tickets_response = ZendeskApiCallHelper._get_api_call(cursor_link)
        return {'tickets':tickets_response, 'info': count_response}

    @staticmethod
    def get_ticket_by_id(id):
        """Method to call API to get a particular ticket based on ID"""
        return ZendeskApiCallHelper._get_api_call(f"https://zcctest.zendesk.com/api/v2/tickets/{id}")


    @staticmethod
    def _get_api_call(endpoint):
        return requests.get(endpoint, auth=requests.auth.HTTPBasicAuth('yjp5077@psu.edu/token', 'F3rYO1svfWLHUuuePCjARgkjr1vl5pxShOj1Bjma')).json()

