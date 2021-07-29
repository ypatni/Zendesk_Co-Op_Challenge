from pytest_mock import MockerFixture
from api import ZendeskApiCallHelper


def test_get_ticket_count(mocker: MockerFixture) -> None:
    mock_response = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "_get_api_call", return_value=mock_response)
    assert ZendeskApiCallHelper.get_total_tickets_count() == mock_response
    assert mocked_function.call_count == 1
    assert mocked_function.call_args[0][0] == "https://zcctest.zendesk.com/api/v2/tickets/count"
