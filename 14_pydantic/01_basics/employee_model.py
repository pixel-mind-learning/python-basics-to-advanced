from typing import Optional
from pydantic import BaseModel, Field
import re


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Maleesha Sandakalum",
    )
    email: str = Field(
        ...,
        pattern=r"^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$",
        description="Employee Email",
        examples="[EMAIL_ADDRESS]",
    )
    phone: str = Field(..., regex=r"")
    department: Optional[str] = Field(
        None,
        description="Employee Department",
        examples="IT",
    )
    salary: float = Field(
        ...,
        ge=10000,
        le=1000000,
        description="Employee Salary",
        examples=10000.0,
    )
    is_manager: bool = False
