from fastapi import APIRouter
from .schema import LoanRequest, LoanResponse
from .service import calculate_loan_emi

router = APIRouter()

@router.post("/")
async def loan_emi(request: LoanRequest) -> LoanResponse:
    emi = calculate_loan_emi(request.principal, request.rate, request.time)
    return LoanResponse(emi=emi)
