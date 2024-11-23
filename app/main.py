from fastapi import FastAPI
from app.core.config import settings
from app.tools.date_calc.router import router as date_diff_router
from app.tools.loan_emi.router import router as loan_emi_router

app = FastAPI(title="Tool API Platform")

# Register routes for each tool
app.include_router(date_diff_router, prefix="/api/v1/date-diff", tags=["Date Caculator"])
app.include_router(loan_emi_router, prefix="/api/v1/loan-emi", tags=["Loan EMI"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Tool API Platform!"}
