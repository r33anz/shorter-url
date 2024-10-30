from functools import wraps
from fastapi import  HTTPException
from typing import Callable
from database_connection import urls_collection

def count_access(func: Callable):
    @wraps(func)
    async def wrapper(short_code: str, *args, **kwargs):
        result = urls_collection.update_one(
            {"shortCode": short_code},
            {"$inc": {"accessCount": 1}}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="URL not founded")

        return await func(short_code, *args, **kwargs)

    return wrapper

