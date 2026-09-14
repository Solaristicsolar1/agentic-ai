from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Optional, List, Dict

class Patient(BaseModel):
    name: str = Field(min_length = 1, max_length=50, pattern=r"^[A-Za-z]+$")
    email: EmailStr
    age: int
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_detail: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value: EmailStr):
        if not value.endswith("@gmail.com"):
            raise ValueError("Email must be a Gmail address")

        return value

    @field_validator('name')
    @classmethod
    def name_to_lower(cls, name):
        return name.lower()

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age >= 60 and 'emergency' not in model.contact_detail:
            raise ValueError("Patient age 60 and above must have an emergency number")

        return model

def main():
    patient_data1 = {"name": "Samuel", "email": "samuel@gmail.com", "age": 65, "married": False, "allergies": ["Peanuts", "Penicillin"], "contact_detail": {"emergency": "08012345678", "address": "Lagos"}}

    patient1 = Patient(**patient_data1)

    print(patient1.name)

main()