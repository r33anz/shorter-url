from abc import ABC,abstractmethod

class UrlServiceInterface(ABC):
    
    @abstractmethod
    def create_short_url(self,url :str):
        pass

    @abstractmethod
    def get_short_url(self):
        pass
    
    @abstractmethod
    def update_short_url(self):
        pass

    @abstractmethod
    def delete_short_url(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass
