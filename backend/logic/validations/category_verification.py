from backend.models.categories import Category


def is_valid_category(category: Category) -> None:
    if type(category.name) != str:
        return TypeError("Name has to be an string")
    category.name = category.name.strip()
    if len(category.name) > 100:
        return ValueError("Name len must be less than 100")
    if len(category.name) == 0:
        return ValueError("Name cannot be null")
    
    return True
