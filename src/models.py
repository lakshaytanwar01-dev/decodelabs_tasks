from typing import Literal
from pydantic import BaseModel, Field, field_validator


Platform = Literal["LinkedIn", "Instagram", "Email"]


class CopyRequest(BaseModel):
    product_name: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=5, max_length=5000)

    platform: Platform

    tone: str = Field(
        default="professional",
        min_length=2,
        max_length=40
    )

    temperature: float = Field(
        default=0.5,
        ge=0.0,
        le=2.0
    )

    top_p: float = Field(
        default=0.9,
        ge=0.0,
        le=1.0
    )

    @field_validator("tone")
    @classmethod
    def clean_tone(cls, value):
        return value.strip()


class CopyResponse(BaseModel):
    product_name: str
    platform: Platform
    tone: str
    copy: str