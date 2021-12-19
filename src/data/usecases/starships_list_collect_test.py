from src.domain.usecases import starships_list_collector
from .starships_list_collector import StarshipsListCollector
from src.infra import SwapiApiConsumer

def test_list():
    api_consumer = SwapiApiConsumer()
    starships_list_collector = StarshipsListCollector(api_consumer)

    page = 1
    starships_list_collector.list(page)