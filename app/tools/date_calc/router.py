from fastapi import APIRouter
from .service import (
    calculate_date_difference,
    days_until_event,
    days_since_event,
    detailed_date_difference,
    future_date_from_now,
    past_date_from_now,
    calculate_age,
    business_days_difference,
    next_occurrence,
    countdown_to_event,
    find_zodiac_sign,
    calculate_work_hours,
    calculate_sleep_duration,
    date_difference_in_heartbeats,
    convert_time_zone,
)
from .schema import (
    DateRequest,
    DateRangeRequest,
    DaysResponse,
    DetailedDateDifferenceResponse,
    CountdownResponse,
    ZodiacResponse,
    HoursResponse,
    SleepDurationResponse,
    HeartbeatsResponse,
    ConvertedTimeResponse,
    SleepRequest,
    DateTimeRequest,
)

router = APIRouter()

@router.post("/date-difference", response_model=DaysResponse)
async def date_difference(request: DateRangeRequest):
    days = calculate_date_difference(request.start_date, request.end_date)
    return {"days": days}

@router.post("/days-until", response_model=DaysResponse)
async def days_until(request: DateRequest):
    days = days_until_event(request.date)
    return {"days": days}

@router.post("/days-since", response_model=DaysResponse)
async def days_since(request: DateRequest):
    days = days_since_event(request.date)
    return {"days": days}

@router.post("/detailed-difference", response_model=DetailedDateDifferenceResponse)
async def detailed_difference(request: DateRangeRequest):
    details = detailed_date_difference(request.start_date, request.end_date)
    return details

@router.post("/future-date", response_model=DateRequest)
async def future_date(days: int):
    future = future_date_from_now(days)
    return {"date": future}

@router.post("/past-date", response_model=DateRequest)
async def past_date(days: int):
    past = past_date_from_now(days)
    return {"date": past}

@router.post("/calculate-age", response_model=DetailedDateDifferenceResponse)
async def age_calculator(request: DateRequest):
    age = calculate_age(request.date)
    return age

@router.post("/business-days", response_model=DaysResponse)
async def business_days(request: DateRangeRequest):
    business_days = business_days_difference(request.start_date, request.end_date)
    return {"days": business_days}

@router.post("/next-occurrence", response_model=DateRequest)
async def next_event(request: DateRequest):
    next_date = next_occurrence(request.date)
    return {"date": next_date}

@router.post("/countdown", response_model=CountdownResponse)
async def countdown(request: DateRequest):
    countdown_details = countdown_to_event(request.date)
    return countdown_details

@router.post("/zodiac", response_model=ZodiacResponse)
async def zodiac_finder(request: DateRequest):
    zodiac_sign = find_zodiac_sign(request.date)
    return {"zodiac_sign": zodiac_sign}

@router.post("/work-hours", response_model=HoursResponse)
async def work_hours(request: DateRangeRequest):
    work_hours = calculate_work_hours(request.start_date, request.end_date)
    return {"work_hours": work_hours}

@router.post("/sleep-duration", response_model=SleepDurationResponse)
async def sleep_tracker(request: SleepRequest):
    sleep_duration = calculate_sleep_duration(request.start_time, request.end_time)
    return sleep_duration

@router.post("/heartbeats", response_model=HeartbeatsResponse)
async def heartbeats(request: DateRangeRequest):
    heartbeats = date_difference_in_heartbeats(request.start_date, request.end_date)
    return {"heartbeats": heartbeats}

@router.post("/time-zone", response_model=ConvertedTimeResponse)
async def time_zone_converter(request: DateTimeRequest):
    converted_time = convert_time_zone(request.date_time, request.from_tz, request.to_tz)
    return {"converted_time": converted_time}

