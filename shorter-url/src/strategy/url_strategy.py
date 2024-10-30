from src.interfaces.strategy_interface import URLShorterStrategyInterface


class UrlStrategy():

    def __init__(self,strategy : URLShorterStrategyInterface):

        self._strategystrategy = strategy

    @property
    def strategy(self) -> URLShorterStrategyInterface:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy:URLShorterStrategyInterface) -> None:
        self._strategy = strategy

    def short_url(self,url : str) -> str:
        self._strategy.url_shorter(url)