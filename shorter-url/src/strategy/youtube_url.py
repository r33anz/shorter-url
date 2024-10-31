from src.interfaces.strategy_interface import URLShorterStrategyInterface
import random
import string
from database_connection import urls_collection
import hashlib

class YoutubeUrlStrategy(URLShorterStrategyInterface):

    def url_shorter(self,url :str) -> str:
        
        prefix = "yt"
        url_hash = hashlib.sha256(url.encode()).hexdigest()[:4]

        while True:
            code = f"{prefix}.{url_hash}.{self.generate_random_code()}"
            if not urls_collection.find_one({"shortCode": code}): 
                return code
        

    def generate_random_code(self,length=6) -> str:

        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    
