from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Literal, Optional, Annotated

class Student(BaseModel):
    name: Annotated[str, Field(pattern=r"^[A-Za-z]+(?:[\s'.\-][A-Za-z]+)*$", min_length=2, max_length=50, description="Name of the student")]
    email: Annotated[EmailStr, Field(description="user's email address")]
    age: Annotated[int, Field(ge=15, le=100)]

    @field_validator("name")
    @classmethod
    def validate_name(cls, name:str) -> str:
        return name.strip().capitalize()

class Course(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50, description="This is the name of the course")]
    level: Literal["beginner", "intermediate", "advanced"]
    price: Annotated[int, Field(ge=10000, default=10000)]
    discount: Annotated[int, Field(ge=0, le=100)]

    @computed_field
    @property
    def price_to_pay(self) -> float:
        discount_price = (self.price * self.discount) / 100
        return self.price - discount_price


class Payment(BaseModel):
    amount: Annotated[int, Field(ge=10000)]
    method: Literal["Transfer", "Cash"]


class Enrollment(BaseModel):
    student: Student
    course: Course
    payment: Payment


    @model_validator(mode="after")
    def validate_payment(self):
        discount_price = (self.course.price * self.course.discount) / 100

        price_to_pay = self.course.price - discount_price

        if price_to_pay != self.payment.amount:
            raise ValueError(
                "Pay the required amount to have access to the course"
            )

        return self


def main():
    student_data = {
        "name": "Samuel",
        "email": "samuel@example.com",
        "age": 25
    }

    student1 = Student(**student_data)

    course_data = {
        "name": "Python",
        "level": "beginner",
        "price": 100000,
        "discount": 10
    }

    student1_course = Course(**course_data)


    payment_data = {
        "amount": 90000,
        "method": "Transfer"
    }

    student1_payment = Payment(**payment_data)

    enrollment = Enrollment(
        student=student1,
        course=student1_course,
        payment=student1_payment
    )

    print(enrollment)
    print(enrollment.model_dump())
    print(enrollment.model_dump_json())

main()

    