from .swapi_api_consumer import SwapApiConsumer

def test_get_starship():
    ''' Testing get_startship method '''
    swapi_api_consumer = SwapApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
