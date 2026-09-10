from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

# class Patient_data(BaseModel):
#     name: str = Field(max_length = 50)
#     email: EmailStr
#     age: int = Field(gt=0, lt=101)
#     weight: float
#     married: bool = False
#     allergies: Optional[List[str]] = Field(max_length = 5)
#     contact: Dict[str, str]


class Patient_data(BaseModel):
    name: Annotated[str, Field(max_length=50, description="The full name of the patient")]
    email: Annotated[EmailStr, Field(description="The patient's email address")]
    age: Annotated[int, Field(gt=0, lt=101, description="The patient's age in years")]
    weight: Annotated[float, Field(description="The patient's weight in kilograms")]
    married: Annotated[bool, Field(description="Whether the patient is married")] = False
    allergies: Annotated[Optional[List[str]], Field(max_length=5, description="A list of the patient's allergies")] = None
    contact: Annotated[Dict[str, str], Field(description="The patient's contact information")]

def add_patient_data(patient: Patient_data):
    print(patient.name)
    print(patient.age)
    print(patient.contact["phone"])
    print("Patient name successfully added to the database")

patient_data = {
    "name": "Samuel",
    "email": "samuel@example.com",
    "age": 100,
    "weight": 72.5,
    "married": False,
    "allergies": ["Penicillin", "Peanuts"],
    "contact": {
        "phone": "08012345678",
        "email": "samuel@example.com"
    }
}

patient = Patient_data(**patient_data)

add_patient_data(patient)