from src.interfaces.strategy_interface import URLShorterStrategyInterface

class YoutubeUrlStrategy(URLShorterStrategyInterface):

    def url_shorter(self,url :str) -> str:
        return "short_youtube_url"