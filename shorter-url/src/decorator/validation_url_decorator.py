from functools import wraps
from typing import Callable
from urllib.parse import urlparse
from fastapi import  HTTPException

def validate_url(fun: Callable):
    @wraps(fun)
    async def wrapper(url: str, *args,**kargs):
        result = urlparse(url)

        if not result.netloc or  not result.scheme:
            raise HTTPException(status_code=404, detail="URL not valid")

        return await fun(url, *args,**kargs)

    return wrapper