import requests

class SwapApiConsumer:

    @classmethod
    def get_starships(self, page: int) -> any:
        params = {'page': page}
        response = requests.get('https://gorest.co.in/public/v1/users', params=params)
        
        return response.json()