from database_connection import urls_collection
from src.strategy.instagram_url import InstagramUrlStrategy
from src.strategy.youtube_url import YoutubeUrlStrategy
from src.interfaces.strategy_interface import URLShorterStrategyInterface
from src.dto.url_dto import UlrResponseDTO

class UrlService():

    def __init__(self):
        self.strategies = {
            "instagram": InstagramUrlStrategy(),
            "youtube": YoutubeUrlStrategy()
        }

    def generate_short_url(self, typeU :str,url:str) -> str:
        strategy: URLShorterStrategyInterface = self.strategies.get(typeU)

        if strategy:

            return strategy.url_shorter(url)
        else:

            raise ValueError(f"Don't find strategy to encode the type url: {type}")
        
    def indentify_url_type(self, url :str):

        if "instagram" in url:

            return "instagram"
        elif "youtube" in url:

            return "youtube"
        else:

            raise ValueError("Unknow url type")

    def create_short_url(self, url :str):

        typeUrl = self.indentify_url_type(url)
        resultUrl = self.generate_short_url(typeUrl,url)
        urls_collection.insert_one({"url": url, "shortCode": resultUrl})

        result = {
            "url": url,
            "shortCode": resultUrl,
            "accessCount": 0 
        }

        return result
    
    def get_short_url(self, short_url :str):
        pass

    def update_short_url(self, short_url :str):
        pass

    def delete_short_url(self, short_url :str):
        pass

    def get_stats(self, short_url :str):
        pass
