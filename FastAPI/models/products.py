from pydantic import BaseModel

class Product(BaseModel):
    """
    Data model for a product.
    Attributes:
    - id: Unique identifier for the product.
    - name: Product name.
    - description: Product description.
    - price: Product price.
    \nExample:
    {
        "id": 1,
        "name": "Example Product",
        "description": "Description of the example product.",
        "price": 19.99
    }
    """
    id: int
    name: str
    description: str
    price: float

class CreateProduct(BaseModel):
    name: str
    description: str
    price: float