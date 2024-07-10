from backend.data_access.producers import get_all_producers, get_producer_by_id, add_producer, delete_producer, update_producer
from backend.models.producers import Producer
from psycopg2.extras import RealDictCursor
from backend.logic.validations.producers_verification import is_valid_producer
from backend.logic.validations.id_verification import check_id


def get_all_producers_data() -> list[RealDictCursor]:
    return get_all_producers()


def get_producer_data_by_id(id: int) -> RealDictCursor:
    if not (error := check_id(id)):
        return error
    return get_producer_by_id(id)


def create_new_producer(producer: Producer) -> None:
    if not (error := is_valid_producer(producer)):
        return error
    return add_producer(producer)


def delete_producer_data(id: int) -> None:
    if not (error := check_id(id)):
        return error
    return delete_producer(id)


def update_producer_data(id: int, producer: Producer) -> None:
    if not (error := check_id(id)):
        return error
    if not (error := is_valid_producer(producer)):
        return error
    return update_producer(id, producer)