from backend.data_access.producers import get_all_producers, add_producer
from backend.models.producers import Producer

def get_all_producers_data() -> dict:
    return get_all_producers()


def create_new_producer(producer: Producer) -> bool:
    return add_producer(producer.name)
