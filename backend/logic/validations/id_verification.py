def check_id(id: id):
    if type(id) != int:
        return TypeError("ID must be an int")
    if id <= 0:
        return ValueError("ID must be positive")
    
    return True