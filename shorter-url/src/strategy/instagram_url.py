from src.interfaces.strategy_interface import URLShorterStrategyInterface
import random
import string
from database_connection import urls_collection
import hashlib

class InstagramUrlStrategy(URLShorterStrategyInterface):

    def url_shorter(self,url :str) -> str:
        prefix = "ig"
        hash_code = hashlib.md5(url.encode()).hexdigest()[:6]
        
        return f"{prefix}.{hash_code}"
            
    
        