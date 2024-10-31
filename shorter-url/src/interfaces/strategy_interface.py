from abc import ABC,abstractmethod

class URLShorterStrategyInterface(ABC):

    @abstractmethod
    def url_shorter(self,url : str) -> str:
        pass

    def generate_random_code(self):
        pass


