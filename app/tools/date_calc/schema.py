from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime

# Base schemas with validation
class DateRequest(BaseModel):
    date: str

    # Validate date format
    @field_validator("date", mode="before")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError(f"'{value}' is not a valid date in the format YYYY-MM-DD.")

class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str

    # Validate start_date format
    @field_validator("start_date", mode="before")
    @classmethod
    def validate_start_date_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError(f"'{value}' is not a valid start_date in the format YYYY-MM-DD.")

    # Validate end_date format
    @field_validator("end_date", mode="before")
    @classmethod
    def validate_end_date_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError(f"'{value}' is not a valid end_date in the format YYYY-MM-DD.")

    # Validate that start_date is before or equal to end_date
    @field_validator("end_date", mode="after")
    @classmethod
    def validate_date_order(cls, value: str, info) -> str:
        start_date = datetime.strptime(info.data["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(value, "%Y-%m-%d")
        if end_date < start_date:
            raise ValueError("end_date must not be earlier than start_date.")
        return value

# Response schemas
class DaysResponse(BaseModel):
    days: int

class DetailedDateDifferenceResponse(BaseModel):
    days: int
    weeks: int
    months: int
    years: int

class CountdownResponse(BaseModel):
    days: int
    hours: int
    minutes: int
    seconds: int

# ✅ Validate datetime format and timezones
class DateTimeRequest(BaseModel):
    date_time: str
    from_tz: str
    to_tz: str

    @field_validator("date_time", mode="before")
    @classmethod
    def validate_datetime_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
            return value
        except ValueError:
            raise ValueError(f"'{value}' is not a valid datetime in the format YYYY-MM-DD HH:MM:SS.")

    @field_validator("from_tz", "to_tz")
    @classmethod
    def validate_timezone(cls, value: str) -> str:
        valid_timezones = ["UTC", "Asia/Phnom_Penh", "America/New_York", "Europe/London"]
        if value not in valid_timezones:
            raise ValueError(f"'{value}' is not a supported timezone.")
        return value


# ✅ Validate sleep start and end times
class SleepRequest(BaseModel):
    start_time: str
    end_time: str

    @field_validator("start_time", "end_time", mode="before")
    @classmethod
    def validate_time_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%H:%M")  # Format: HH:MM
            return value
        except ValueError:
            raise ValueError(f"'{value}' is not a valid time in the format HH:MM.")

    @field_validator("end_time", mode="after")
    @classmethod
    def validate_time_order(cls, value: str, info) -> str:
        start_time = datetime.strptime(info.data["start_time"], "%H:%M")
        end_time = datetime.strptime(value, "%H:%M")
        if end_time <= start_time:
            raise ValueError("end_time must be after start_time.")
        return value
# Response schemas
class ZodiacResponse(BaseModel):
    zodiac_sign: str

class HoursResponse(BaseModel):
    work_hours: int

class SleepDurationResponse(BaseModel):
    hours: int
    minutes: int

class HeartbeatsResponse(BaseModel):
    heartbeats: int

class ConvertedTimeResponse(BaseModel):
    converted_time: str