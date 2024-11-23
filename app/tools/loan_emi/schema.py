from pydantic import BaseModel

class LoanRequest(BaseModel):
    principal: float
    rate: float
    time: int

class LoanResponse(BaseModel):
    emi: float
