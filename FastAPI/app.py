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
    """
    Method to return all registered products.
    """
    return data

@app.get("/api/products/{product_id}")
def get_products_by_id(product_id: int):
    """
    Method to return product information using the ID passed as a parameter.
    """
    for product in data:
        if product.id == product_id:
            return product
    return {"message": "No product found with this ID."}

@app.post("/api/products")
def create_product(product: CreateProduct):
    """
    Method to create a new product.
    """
    new_product = Product(id=len(data)+1, **product.dict())
    data.append(new_product)
    return new_product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    """
    Method to delete a product using the ID passed as a parameter.
    """
    for i, product in enumerate(data):
        if product.id == product_id:
            deleted_product = data.pop(i)
            return{
                'message': 'Product deleted successfully!',
                'deleted product': deleted_product
            }
    return {
        'message': 'No product found with this ID.'
    }

@app.put("/api/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    """
    Method to update a product using the ID passed as a parameter.
    """
    for i, product in enumerate(data):
        if product.id == product_id:
            data[i] = updated_product
            return{
                'message': 'Product updated successfully!',
                'updated product': updated_product
            }
    return {
        'message': 'No product found with this ID.'
    }