from fastapi.routing import APIRouter
from backend.apis.utils.status_response import status_response
from backend.apis.utils.data_response import data_response
from backend.logic.producers import get_all_producers_data, get_producer_data_by_id, create_new_producer, delete_producer_data, update_producer_data
from backend.models.producers import Producer

router = APIRouter()

@router.get("/producers")
async def get_producers():
    data = get_all_producers_data()
    return data_response(data)


@router.get("/producers/{id}")
async def get_producer_by_id(id: int):
    data = get_producer_data_by_id(id)
    return data_response(data)


@router.post("/producers")
async def post_producers(producer: Producer):
    status = create_new_producer(producer)
    return status_response(status)
    
    
@router.delete("/producers/{id}")
async def delete_producer(id: int):
    status = delete_producer_data(id)
    return status_response(status)
    
    
@router.put("/producers/{id}")
async def put_producer(id: int, producer: Producer):
    status = update_producer_data(id, producer)
    return status_response(status)