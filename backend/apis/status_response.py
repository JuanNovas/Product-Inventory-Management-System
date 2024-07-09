from fastapi import HTTPException


def status_response(status):
    if not isinstance(status, Exception):
        return {"status" : "ok"}
    else:
        raise HTTPException(status_code=400, detail=str(status))