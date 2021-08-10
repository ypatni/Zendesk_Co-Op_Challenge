from pytest_mock import MockerFixture
from api import ZendeskApiCallHelper


def test_get_ticket_count(mocker: MockerFixture) -> None:
    """Testing ticket count API call"""
    mock_response = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "_get_api_call", return_value=mock_response)
    assert ZendeskApiCallHelper.get_total_tickets_count() == mock_response
    assert mocked_function.call_count == 1
    assert mocked_function.call_args[0][0] == "https://zcctestsupport.zendesk.com/api/v2/tickets/count"

def test_get_ticket_by_id(mocker: MockerFixture) -> None:
    """Testing get ticket by ID API call"""
    mock_response = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "_get_api_call", return_value=mock_response)
    assert ZendeskApiCallHelper.get_ticket(3) == mock_response
    assert mocked_function.call_count == 1
    assert mocked_function.call_args[0][0] == "https://zcctestsupport.zendesk.com/api/v2/tickets/3"

def test_get_tickets(mocker: MockerFixture) -> None:
    """Test get tickets function for an input link"""
    mock_response_count = mocker.MagicMock()
    mock_response_api_call = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_total_tickets_count", return_value=mock_response_count)
    mocked_api_function = mocker.patch.object(ZendeskApiCallHelper, "_get_api_call", return_value=mock_response_api_call)
    assert ZendeskApiCallHelper.get_total_tickets_count() == mock_response_count
    assert ZendeskApiCallHelper.get_tickets('mock_call')['tickets'] == mock_response_api_call
    assert ZendeskApiCallHelper.get_tickets('mock_call')['info'] == mock_response_count
    assert mocked_api_function.call_args[0][0] == 'mock_call'

def test_get_tickets_none(mocker: MockerFixture) -> None:
    """Test get tickets function for an NO input link"""
    mock_response_count = mocker.MagicMock()
    mock_response_api_call = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_total_tickets_count", return_value=mock_response_count)
    mocked_api_function = mocker.patch.object(ZendeskApiCallHelper, "_get_api_call", return_value=mock_response_api_call)
    assert ZendeskApiCallHelper.get_total_tickets_count() == mock_response_count
    assert ZendeskApiCallHelper.get_tickets(None)['tickets'] == mock_response_api_call
    assert mocked_api_function.call_args[0][0] == 'https://zcctestsupport.zendesk.com/api/v2/tickets.json?page[size]=25'