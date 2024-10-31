from src.interfaces.url_service_interface import UrlServiceInterface
from src.decorator.count_decorator import count_access
from src.dto.url_dto import UlrResponseDTO,UrlCreateDTO
from fastapi import  HTTPException , status

class UrlController():

    def __init__(self,urlService : UrlServiceInterface):
        self.service = urlService

    def create_short_url(self, url: str) -> UlrResponseDTO:
        result = self.service.create_short_url(url)
        if not result:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create short URL")
        return UlrResponseDTO(**result)

    @count_access
    def get_short_url(self, short_url: str) -> UlrResponseDTO:

        result = self.service.get_short_url(short_url)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
        return UlrResponseDTO(**result)
    
    def get_all_url(self):

        documents = self.service.get_all_url()
        return [UlrResponseDTO(**doc) for doc in documents ]

    def update_short_url(self, short_url: str, url : str) -> UlrResponseDTO:

        result = self.service.update_short_url(short_url, url)

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
        
        return UlrResponseDTO(**result)

    def delete_short_url(self, short_url: str):

        success = self.service.delete_short_url(short_url)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
        return None  
    
    def get_stats(self, short_url: str) -> UlrResponseDTO:

        stats = self.service.get_stats(short_url)
        if not stats:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Statistics not found")
        return UlrResponseDTO(**stats)
