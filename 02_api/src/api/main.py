from fastapi import FastAPI
from src.api import endpoints

app = FastAPI(title="BMI Calculation API")

# Include the endpoints
app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the BMI Calculation API. Use /calculate to compute BMI."}
