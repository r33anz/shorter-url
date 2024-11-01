from database_connection import urls_collection
from src.strategy.instagram_url import InstagramUrlStrategy
from src.strategy.youtube_url import YoutubeUrlStrategy
from src.interfaces.strategy_interface import URLShorterStrategyInterface
from src.interfaces.url_service_interface import UrlServiceInterface
from src.decorator.count_decorator import count_access

class UrlService(UrlServiceInterface):

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

        result = {
            "url": url,
            "shortCode": resultUrl,
            "accessCount": 0 
        }

        urls_collection.insert_one(result)
        return result
    
    
    def get_short_url(self,short_url :str):

        document = urls_collection.find_one({"shortCode": short_url})

        if not document:
            return None
        
        return document

    def get_all_url(self):
        documents = urls_collection.find()
        return documents

    def update_short_url(self, short_url :str, url : str):

        result = urls_collection.update_one(
            { "shortCode": short_url },
            { "$set": { "url": url } }
        )

        if result.modified_count == 0:
            return None 

        updated_document = urls_collection.find_one({"shortCode": short_url})

        return updated_document


    def delete_short_url(self, short_url :str):
        
        result = urls_collection.delete_one({ "shortCode": short_url })
        return result

    def get_stats(self, short_url :str):
        document = urls_collection.find_one({"shortCode": short_url})

        if not document:
            return None
        
        return document
