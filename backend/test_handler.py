from handler import get_tickets


def test_get_tickets_handler():
    response = get_tickets(
        {
            'body': {
    "cursor": "https://zcctest.zendesk.com/api/v2/tickets.json?page%5Bafter%5D=eyJvIjoibmljZV9pZCIsInYiOiJhUmtBQUFBQUFBQUEifQ%3D%3D&page%5Bsize%5D=25"
            }
        }, {}
    )
    assert response["statusCode"] == 200
