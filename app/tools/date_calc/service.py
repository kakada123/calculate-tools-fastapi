from datetime import datetime, timedelta
from pytz import timezone

# Calculate date difference in days
def calculate_date_difference(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days

# Calculate days until an event
def days_until_event(event_date: str) -> int:
    event = datetime.strptime(event_date, "%Y-%m-%d")
    today = datetime.now()
    return (event - today).days

# Calculate days since an event
def days_since_event(event_date: str) -> int:
    event = datetime.strptime(event_date, "%Y-%m-%d")
    today = datetime.now()
    return (today - event).days

# Calculate detailed difference
def detailed_date_difference(start_date: str, end_date: str) -> dict:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start

    days = delta.days
    weeks = days // 7
    months = days // 30  # Approximation
    years = days // 365  # Approximation

    return {"days": days, "weeks": weeks, "months": months, "years": years}

# Future date from now
def future_date_from_now(days_to_add: int) -> str:
    future_date = datetime.now() + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

# Past date from now
def past_date_from_now(days_to_subtract: int) -> str:
    past_date = datetime.now() - timedelta(days=days_to_subtract)
    return past_date.strftime("%Y-%m-%d")

# Calculate age
def calculate_age(birth_date: str) -> dict:
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    if months < 0:
        years -= 1
        months += 12
    if days < 0:
        months -= 1
        days += (birth.replace(month=today.month) - birth.replace(month=today.month - 1)).days

    # Calculate total days and derive weeks
    total_days = (today - birth.replace(year=today.year)).days
    weeks = total_days // 7

    return {"years": years, "months": months, "days": days, "weeks": weeks}

# Business days difference
def business_days_difference(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    business_days = 0

    current = start
    while current <= end:
        if current.weekday() < 5:  # Monday-Friday
            business_days += 1
        current += timedelta(days=1)
    return business_days

# Next occurrence of an annual event
def next_occurrence(event_date: str) -> str:
    event = datetime.strptime(event_date, "%Y-%m-%d")
    today = datetime.now()
    next_event = event.replace(year=today.year)
    if next_event < today:
        next_event = next_event.replace(year=today.year + 1)
    return next_event.strftime("%Y-%m-%d")

# Countdown to an event
def countdown_to_event(event_date: str) -> dict:
    event = datetime.strptime(event_date, "%Y-%m-%d")
    now = datetime.now()

    # Check if the event is in the past or future
    if event < now:
        delta = now - event  # Time since the event
        sign = -1
    else:
        delta = event - now  # Time until the event
        sign = 1

    days = delta.days * sign
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    # Adjust the sign for past events
    return {
        "days": days,
        "hours": hours if sign == 1 else -hours,
        "minutes": minutes if sign == 1 else -minutes,
        "seconds": seconds if sign == 1 else -seconds,
    }

## Find Zodiac
def find_zodiac_sign(birth_date: str) -> str:
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    month = date.month
    day = date.day

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"
 
### Calculate work hours   
def calculate_work_hours(start_date: str, end_date: str, hours_per_day: int = 8) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    total_days = (end - start).days + 1

    # Exclude weekends (Saturday and Sunday)
    work_days = sum(1 for day in range(total_days) if (start + timedelta(days=day)).weekday() < 5)
    return work_days * hours_per_day

### Sleep Duration
def calculate_sleep_duration(start_time: str, end_time: str) -> dict:
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")

    if end < start:
        end += timedelta(days=1)  # Handle overnight sleep

    duration = end - start
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60

    return {"hours": hours, "minutes": minutes}

### Date calculate in different units
def date_difference_in_heartbeats(start_date: str, end_date: str, bpm: int = 70) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    total_minutes = (end - start).total_seconds() / 60

    return int(total_minutes * bpm)

def convert_time_zone(date_time: str, from_tz: str, to_tz: str) -> str:
    dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    from_zone = timezone(from_tz)
    to_zone = timezone(to_tz)

    localized_dt = from_zone.localize(dt)
    converted_dt = localized_dt.astimezone(to_zone)

    return converted_dt.strftime("%Y-%m-%d %H:%M:%S")
