from pydantic import BaseModel
from typing import Optional, List, Union


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: int
    country: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    email: str
    company: Optional[Company] = None


class TextContent(BaseModel):
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt: str


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Organization(BaseModel):
    name: str
    headquarters: City


class Department(BaseModel):
    name: str
    manager: str
    organization: Organization


if __name__ == "__main__":
    # Example input data containing a list of different content types for the Union
    article_data = {
        "title": "Mastering Pydantic Unions",
        "sections": [
            {
                "type": "text",
                "content": "Pydantic is a powerful data validation library.",
            },
            {
                "type": "image",
                "url": "https://example.com/logo.png",
                "alt": "Pydantic Logo",
            },
            {
                "type": "text",
                "content": "Unions allow fields to accept multiple different structures.",
            },
        ],
    }

    # Parse and validate the dictionary using the Article model
    article = Article(**article_data)

    print(f"--- Article: {article.title} ---")
    for i, section in enumerate(article.sections, 1):
        print(f"Section {i}: Type = {type(section).__name__}")
        print(f"Details: {section.model_dump()}\n")
