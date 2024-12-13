from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EXCHANGE_RATES = {
    "USD": {"EUR": 0.9, "INR": 83.0, "JPY": 110.0, "NPR": 133.0},
    "EUR": {"USD": 1.11, "INR": 92.2, "JPY": 123.4, "NPR": 148.0},
    "INR": {"USD": 0.012, "EUR": 0.011, "JPY": 1.5, "NPR": 1.6},
    "JPY": {"USD": 0.009, "EUR": 0.008, "INR": 0.67, "NPR": 0.9},
    "NPR": {"USD": 0.0075, "EUR": 0.0068, "INR": 0.625, "JPY": 1.1},
}

class ConversionRequest(BaseModel):
    from_currency:str
    to_currency: str
    amount: float

@app.get("/currencies")
def get_currencies():
    return {"currencies":list(EXCHANGE_RATES)}

@app.post("/convert")
def convert_currency(request:ConversionRequest):
    from_currency = request.from_currency
    to_currency = request.to_currency
    amount = request.amount
    
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise HTTPException(status_code=400, detail="Invalid currency pair")
    
    converted_amount = amount * EXCHANGE_RATES[from_currency][to_currency]
    return {"converted_amount": converted_amount} 

