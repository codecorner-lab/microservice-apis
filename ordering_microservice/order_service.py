from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Order(BaseModel):
    product: str
    quantity: int
    price: float

PAYMENT_SERVICE_URLS = ["http://localhost:8001/pay", "http://payment_service:8001/pay"]

@app.post("/create-order/")
async def create_order(order: Order):
    total_price = order.quantity * order.price

    for url in PAYMENT_SERVICE_URLS:
        try:
            payment_response = requests.post(url, json={"amount": total_price})
            if payment_response.status_code == 200:
                return {"status": "Order placed successfully", "order": order}
        except requests.exceptions.ConnectionError:
            continue

    return {"status": "Payment failed, could not reach payment service"}