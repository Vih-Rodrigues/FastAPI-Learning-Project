from fastapi import FastAPI
from models.products import Product, CreateProduct

app = FastAPI()

data = [
    Product(id=1, name="Product 1", description="product 1", price=10.0),
    Product(id=2, name="Product 2", description="product 2", price=20.0),
    Product(id=3, name="Product 3", description="product 3", price=30.0),
]

@app.get("/api/products") # API index
def get_products():
    return data

@app.get("/api/products/{product_id}")
def get_products_by_id(product_id: int):
    for product in data:
        if product.id == product_id:
            return product
    return {"message": "No product found with this ID."}

@app.post("/api/products")
def create_product(product: CreateProduct):
    new_product = Product(id=len(data)+1, **product.dict())
    data.append(new_product)
    return new_product