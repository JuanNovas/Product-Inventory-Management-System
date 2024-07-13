from backend.models.producers import Producer


def is_valid_producer(producer: Producer) -> None:
    if type(producer.name) != str:
        return TypeError("Name must be a string")
    producer.name = producer.name.strip()
    if len(producer.name) > 100:
        return ValueError("Name len must be less than 101")
    if len(producer.name) == 0:
        return ValueError("Name cannot be null")
    
    return True