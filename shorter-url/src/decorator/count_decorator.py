from functools import wraps
from fastapi import  HTTPException
from typing import Callable
from database_connection import urls_collection

def count_access(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
       
        short_code =  (args[1] if len(args) > 1 else None)

        result = urls_collection.update_one(
            {"shortCode": short_code},
            {"$inc": {"accessCount": 1}}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="URL not founded")

        return  func(*args, **kwargs)

    return wrapper

