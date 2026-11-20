from fastapi import FastAPI, HTTPException

app = FastAPI(title="Product Service", version="1.0")

# Mock database for products
products_db = {
    101: {"id": 101, "name": "Mechanical Keyboard", "price": 120.00},
    102: {"id": 102, "name": "Wireless Mouse", "price": 45.50},
}


@app.get("/products/{product_id}")
def get_product(product_id: int):
  if product_id not in products_db:
    raise HTTPException(status_code=404, detail="Product not found")
  return products_db[product_id]