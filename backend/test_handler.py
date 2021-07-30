from handler import get_tickets
from handler import get_ticket_by_id
from pytest_mock import MockerFixture
from api import ZendeskApiCallHelper

import json

def test_get_tickets_handler_error(mocker: MockerFixture) -> None:
    """Test get tickets handler for incorrect response"""
    mock_response = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_tickets", return_value=mock_response)
    response = get_tickets(
        {
            'body': json.dumps({"cursor": 'mock cursor'})
        }, {}
    )
    assert mocked_function.call_count == 1
    assert response == {'statusCode': 500, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': True}, 'body': '"Object of type MagicMock is not JSON serializable"'}

def test_get_tickets_handler_success(mocker: MockerFixture) -> None:
    """Test get tickets handler for correct response"""
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_tickets", return_value={})
    response = get_tickets(
        {
            'body': json.dumps({"cursor": 'mock cursor'})
        }, {}
    )
    assert mocked_function.call_count == 1
    assert response == {'body': '{}',
 'headers': {'Access-Control-Allow-Credentials': True,
             'Access-Control-Allow-Origin': '*'},
 'statusCode': 200}

def test_get_ticket_success(mocker: MockerFixture) -> None:
    """Test get single ticket info handler for correct response"""
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_ticket_by_id", return_value={})
    response = get_ticket_by_id(
        {'resource': '/tickets/{id}', 'path': '/tickets/1', 'httpMethod': 'GET',
         'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9',
                     'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true',
                     'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false',
                     'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US',
                     'Host': 'faq1slxbph.execute-api.us-east-1.amazonaws.com', 'origin': 'http://localhost:3000',
                     'Referer': 'http://localhost:3000/',
                     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                     'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'cross-site',
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                     'Via': '2.0 27f5831be5a9ad411fca9c84fe627bdc.cloudfront.net (CloudFront)',
                     'X-Amz-Cf-Id': '31c5JvO6KQbQjpWEdc5Rey0VW6PvAO8g1OhX6YSkVV4kZZseAeXoEw==',
                     'X-Amzn-Trace-Id': 'Root=1-6101a0bb-31d3485b54b5fd8866015641',
                     'X-Forwarded-For': '76.124.168.93, 52.46.46.111', 'X-Forwarded-Port': '443',
                     'X-Forwarded-Proto': 'https'},
         'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'],
                               'Accept-Language': ['en-US,en;q=0.9'], 'CloudFront-Forwarded-Proto': ['https'],
                               'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'],
                               'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'],
                               'CloudFront-Viewer-Country': ['US'],
                               'Host': ['faq1slxbph.execute-api.us-east-1.amazonaws.com'],
                               'origin': ['http://localhost:3000'], 'Referer': ['http://localhost:3000/'],
                               'sec-ch-ua': ['" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'],
                               'sec-ch-ua-mobile': ['?0'], 'sec-fetch-dest': ['empty'], 'sec-fetch-mode': ['cors'],
                               'sec-fetch-site': ['cross-site'], 'User-Agent': [
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'],
                               'Via': ['2.0 27f5831be5a9ad411fca9c84fe627bdc.cloudfront.net (CloudFront)'],
                               'X-Amz-Cf-Id': ['31c5JvO6KQbQjpWEdc5Rey0VW6PvAO8g1OhX6YSkVV4kZZseAeXoEw=='],
                               'X-Amzn-Trace-Id': ['Root=1-6101a0bb-31d3485b54b5fd8866015641'],
                               'X-Forwarded-For': ['76.124.168.93, 52.46.46.111'], 'X-Forwarded-Port': ['443'],
                               'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None,
         'multiValueQueryStringParameters': None, 'pathParameters': {'id': '1'}, 'stageVariables': None,
         'requestContext': {'resourceId': 'ciwo05', 'resourcePath': '/tickets/{id}', 'httpMethod': 'GET',
                            'extendedRequestId': 'DMYNTHvQIAMFV7g=', 'requestTime': '28/Jul/2021:18:23:55 +0000',
                            'path': '/dev/tickets/1', 'accountId': '689157321639', 'protocol': 'HTTP/1.1',
                            'stage': 'dev', 'domainPrefix': 'faq1slxbph', 'requestTimeEpoch': 1627496635393,
                            'requestId': '5d8d4dbd-d712-40a6-8a64-a6a1f5f6450d',
                            'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None,
                                         'caller': None, 'sourceIp': '76.124.168.93', 'principalOrgId': None,
                                         'accessKey': None, 'cognitoAuthenticationType': None,
                                         'cognitoAuthenticationProvider': None, 'userArn': None,
                                         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                                         'user': None}, 'domainName': 'faq1slxbph.execute-api.us-east-1.amazonaws.com',
                            'apiId': 'faq1slxbph'}, 'body': None, 'isBase64Encoded': False}, {}
    )
    assert mocked_function.call_count == 1
    assert response == {'body': '{}',
                        'headers': {'Access-Control-Allow-Credentials': True,
                                    'Access-Control-Allow-Origin': '*'},
                        'statusCode': 200}

def test_get_ticket_error(mocker: MockerFixture) -> None:
    """Test get single ticket info handler for incorrect response"""
    mock_response = mocker.MagicMock()
    mocked_function = mocker.patch.object(ZendeskApiCallHelper, "get_ticket_by_id", return_value=mock_response)
    response = get_ticket_by_id(
        {'resource': '/tickets/{id}', 'path': '/tickets/1', 'httpMethod': 'GET',
         'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9',
                     'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true',
                     'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false',
                     'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US',
                     'Host': 'faq1slxbph.execute-api.us-east-1.amazonaws.com', 'origin': 'http://localhost:3000',
                     'Referer': 'http://localhost:3000/',
                     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                     'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'cross-site',
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                     'Via': '2.0 27f5831be5a9ad411fca9c84fe627bdc.cloudfront.net (CloudFront)',
                     'X-Amz-Cf-Id': '31c5JvO6KQbQjpWEdc5Rey0VW6PvAO8g1OhX6YSkVV4kZZseAeXoEw==',
                     'X-Amzn-Trace-Id': 'Root=1-6101a0bb-31d3485b54b5fd8866015641',
                     'X-Forwarded-For': '76.124.168.93, 52.46.46.111', 'X-Forwarded-Port': '443',
                     'X-Forwarded-Proto': 'https'},
         'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'],
                               'Accept-Language': ['en-US,en;q=0.9'], 'CloudFront-Forwarded-Proto': ['https'],
                               'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'],
                               'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'],
                               'CloudFront-Viewer-Country': ['US'],
                               'Host': ['faq1slxbph.execute-api.us-east-1.amazonaws.com'],
                               'origin': ['http://localhost:3000'], 'Referer': ['http://localhost:3000/'],
                               'sec-ch-ua': ['" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'],
                               'sec-ch-ua-mobile': ['?0'], 'sec-fetch-dest': ['empty'], 'sec-fetch-mode': ['cors'],
                               'sec-fetch-site': ['cross-site'], 'User-Agent': [
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'],
                               'Via': ['2.0 27f5831be5a9ad411fca9c84fe627bdc.cloudfront.net (CloudFront)'],
                               'X-Amz-Cf-Id': ['31c5JvO6KQbQjpWEdc5Rey0VW6PvAO8g1OhX6YSkVV4kZZseAeXoEw=='],
                               'X-Amzn-Trace-Id': ['Root=1-6101a0bb-31d3485b54b5fd8866015641'],
                               'X-Forwarded-For': ['76.124.168.93, 52.46.46.111'], 'X-Forwarded-Port': ['443'],
                               'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None,
         'multiValueQueryStringParameters': None, 'pathParameters': {'id': '1'}, 'stageVariables': None,
         'requestContext': {'resourceId': 'ciwo05', 'resourcePath': '/tickets/{id}', 'httpMethod': 'GET',
                            'extendedRequestId': 'DMYNTHvQIAMFV7g=', 'requestTime': '28/Jul/2021:18:23:55 +0000',
                            'path': '/dev/tickets/1', 'accountId': '689157321639', 'protocol': 'HTTP/1.1',
                            'stage': 'dev', 'domainPrefix': 'faq1slxbph', 'requestTimeEpoch': 1627496635393,
                            'requestId': '5d8d4dbd-d712-40a6-8a64-a6a1f5f6450d',
                            'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None,
                                         'caller': None, 'sourceIp': '76.124.168.93', 'principalOrgId': None,
                                         'accessKey': None, 'cognitoAuthenticationType': None,
                                         'cognitoAuthenticationProvider': None, 'userArn': None,
                                         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                                         'user': None}, 'domainName': 'faq1slxbph.execute-api.us-east-1.amazonaws.com',
                            'apiId': 'faq1slxbph'}, 'body': None, 'isBase64Encoded': False}, {}
    )
    assert mocked_function.call_count == 1
    assert response == {'statusCode': 500, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': True}, 'body': '"Object of type MagicMock is not JSON serializable"'}
