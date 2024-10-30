from abc import ABC,abstractmethod

class URLShorterStrategyInterface(ABC):

    @abstractmethod
    def url_shorter(url : str) -> str:
        pass


