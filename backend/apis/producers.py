from fastapi.routing import APIRouter, HTTPException
from backend.logic.producers import get_all_producers_data, create_new_producer
from backend.models.producers import Producer

router = APIRouter()

@router.get("/producers")
async def get_producers():
    data = get_all_producers_data()
    return data


@router.post("/producers")
async def post_producers(producer: Producer):
    status = create_new_producer(producer)
    if not isinstance(status, Exception):
        return {"status" : "ok"}
    else:
        raise HTTPException(status_code=400, detail=str(status))