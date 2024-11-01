from fastapi import APIRouter , HTTPException , status
from src.controllers.url_controller import UrlController
from src.services.url_service import UrlService
from src.dto.url_dto import UlrResponseDTO,UrlCreateDTO,UlrResponseStatsDTO
from typing import List

router = APIRouter()

urlService = UrlService()
urlController = UrlController(urlService) 

@router.get('/shorten/{short_url}', response_model=UlrResponseDTO)
def get_short_url(short_url: str):
    return  urlController.get_short_url(short_url)

@router.get('/shorten/{short_url}/stats', response_model=UlrResponseStatsDTO)
def url_stats(short_url: str):
    return urlController.get_stats(short_url)

@router.get('/shorten',response_model=List[UlrResponseDTO])
def get_all_url():
    return urlController.get_all_url()

@router.post('/shorten', response_model=UlrResponseDTO, status_code=status.HTTP_201_CREATED)
def create_url(url: str):
    return urlController.create_short_url(url)

@router.put('/shorten/{short_url}', response_model=UlrResponseDTO)
def update_url(short_url: str, url : UrlCreateDTO):
    return urlController.update_short_url(short_url,url.url)

@router.delete('/shorten/{short_url}', status_code=status.HTTP_204_NO_CONTENT)
def delete_url(short_url: str):
    return urlController.delete_short_url(short_url)
