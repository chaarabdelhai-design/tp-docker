import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Gateway", version="1.0")

# Pull from environment variables set in docker-compose.yml
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8001")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8002")


@app.get("/api/users/{user_id}")
async def gateway_get_user(user_id: int):
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
    except httpx.RequestError:
      raise HTTPException(
          status_code=503, detail="User Service is currently unavailable"
      )

    if response.status_code != 200:
      raise HTTPException(
          status_code=response.status_code, detail=response.json()
      )
    return response.json()


@app.get("/api/products/{product_id}")
async def gateway_get_product(product_id: int):
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    except httpx.RequestError:
      raise HTTPException(
          status_code=503, detail="Product Service is currently unavailable"
      )

    if response.status_code != 200:
      raise HTTPException(
          status_code=response.status_code, detail=response.json()
      )
    return response.json()