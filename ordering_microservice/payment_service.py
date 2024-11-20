from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    amount: float

@app.post("/pay/")
async def process_payment(payment: Payment):
    if payment.amount > 0:
        return {"status": "Payment process successfully"}
    return {"status": "Payment failed"}