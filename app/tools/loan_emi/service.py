def calculate_loan_emi(principal: float, rate: float, time: int) -> float:
    monthly_rate = rate / (12 * 100)
    emi = (principal * monthly_rate * ((1 + monthly_rate)**time)) / (((1 + monthly_rate)**time) - 1)
    return round(emi, 2)
