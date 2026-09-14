from datetime import date
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Dict, List


class Student(BaseModel):

    student_id: Annotated[str, Field(description="Unique identification number assigned to the student")]
    first_name: Annotated[str, Field(pattern=r"^[A-Za-z]+$", min_length=2, max_length=50, description="Student's first name")]
    middle_name: Annotated[str | None, Field(pattern=r"^[A-Za-z]+$", default=None, max_length=50, description="Student's middle name")]
    last_name: Annotated[str, Field(pattern=r"^[A-Za-z]+$", min_length=2, max_length=50, description="Student's surname or last name")]
    gender: Annotated[str, Field(description="Student's gender")]
    email: Annotated[EmailStr, Field(description="Student's university email address")]
    date_of_birth: Annotated[date, Field(description="Student's date of birth")]
    phone_number: Annotated[str | None, Field(default=None, description="Student's phone number")]
    address: Annotated[str | None, Field(default=None, max_length=200, description="Student's residential address")]
    nationality: Annotated[str | None, Field(default=None, description="Student's nationality")]
    state_of_origin: Annotated[str | None, Field(default=None, description="Student's state of origin")]
    faculty: Annotated[str, Field(max_length=100, description="Faculty in which the student is enrolled")]
    department: Annotated[str, Field(max_length=100, description="Department in which the student is enrolled")]
    program: Annotated[str, Field(max_length=100, description="Academic program or degree being studied")]
    level: Annotated[int, Field(ge=100, le=600, description="Student's current academic level")]
    entry_year: Annotated[int, Field(ge=2000, description="Year the student entered the university")]
    expected_graduation_year: Annotated[int | None, Field(default=None, description="Expected year of graduation")]
    student_status: Annotated[str, Field(description="Current status of the student")]
    gpa: Annotated[float | None, Field(default=None, ge=0, le=5, description="Student's cumulative GPA on a 5.0 scale")]
    courses: Annotated[List[str] | None, Field(default=None, description="List of courses currently taken by the student")]
    scores: Annotated[Dict[str, int] | None, Field(default=None, description="Mapping of course names to scores")]
    guardian_name: Annotated[str | None, Field(default=None, max_length=100, description="Name of the student's parent or guardian")]
    guardian_phone: Annotated[str | None, Field(default=None, description="Phone number of the student's parent or guardian")]


def main():
    student_data1 = {"student_id": "OOU/2026/00123", "first_name": "Samuel", "middle_name": "Sodiq", "last_name": "Okafor", "gender": "Male", "email": "samuel.okafor@university.edu", "date_of_birth": "2001-05-23", "phone_number": "08031234567", "address": "Ikeja, Lagos, Nigeria", "nationality": "Nigerian", "state_of_origin": "Ondo", "faculty": "Faculty of Science", "department": "Computer Science", "program": "B.Sc. Computer Science", "level": 300, "entry_year": 2024, "expected_graduation_year": 2028, "student_status": "Active", "gpa": 4.32, "courses": ["Data Structures", "Database Systems", "Computer Networks", "Operating Systems"], "scores": {"Data Structures": 88, "Database Systems": 91, "Computer Networks": 79, "Operating Systems": 85}, "guardian_name": "John Okafor", "guardian_phone": "08039876543"}
    student1 = Student(**student_data1)
    student_profile(student1)

def student_profile(student_data: Student):
    print(student_data.first_name, student_data.last_name)
    print(student_data.gender)
main()