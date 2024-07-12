from fastapi import HTTPException


def data_response(data):
    if not isinstance(data, Exception):
        return data
    else:
        raise HTTPException(status_code=400, detail=str(data))