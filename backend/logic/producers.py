from backend.data_access.producers import get_all_producers, get_producer_by_id, add_producer, delete_producer, update_producer
from backend.models.producers import Producer
from psycopg2.extras import RealDictCursor
from backend.logic.validations.producers_verification import is_valid_producer
from backend.logic.validations.id_verification import check_id


def get_all_producers_data() -> list[RealDictCursor]:
    return get_all_producers()


def get_producer_data_by_id(id: int) -> RealDictCursor:
    if (error := check_id(id)) != True:
        return error
    return get_producer_by_id(id)


def create_new_producer(producer: Producer) -> None:
    if (error := is_valid_producer(producer)) != True:
        return error
    return add_producer(producer)


def delete_producer_data(id: int) -> None:
    if (error := check_id(id)) != True:
        return error
    return delete_producer(id)


def update_producer_data(id: int, producer: Producer) -> None:
    if (error := check_id(id)) != True:
        return error
    if (error := is_valid_producer(producer)) != True:
        return error
    return update_producer(id, producer)