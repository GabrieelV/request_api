from .swapi_api_consumer import SwapApiConsumer

def test_get_starship(requests_mock):
    ''' Testing get_startship method '''

    requests_mock.get('https://gorest.co.in/public/v1/users', status_code=200, json={ 'some': 'thing' })
    swapi_api_consumer = SwapApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
