from .swapi_api_consumer import SwapiApiConsumer
from src.errors import HttpRequestError

def test_get_starships(requests_mock):
    ''' Testing get_startships method '''

    requests_mock.get(
        'https://swapi.dev/api/starships/',
        status_code=200,
        json={ 'some': 'thing', 'results': [{}] }
        )
    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    get_starship_response = swapi_api_consumer.get_starships(page=page)

    assert get_starship_response.request.method == 'GET'
    assert get_starship_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starship_response.request.params == {'page': page}

    assert get_starship_response.status_code == 200
    assert isinstance(get_starship_response.response['results'], list)


def test_get_starships_http_error(requests_mock):
    ''' Testing error in get_starships method '''

    requests_mock.get(
        'https://swapi.dev/api/starships/',
        status_code=404,
        json={ 'detail': 'something' }
        )
    swapi_api_consumer = SwapiApiConsumer()
    page = 100

    try:
        swapi_api_consumer.get_starships(page=page)
        # se não ocorrer erro, força um erro dizendo que o método não está gerando
        # um erro proposital
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
