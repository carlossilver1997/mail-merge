from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class PersonSchema(BaseModel):
    givenNames: str = Field(...)
    lastName1: str = Field(...)
    lastName2: str = Field(...)
    position: str = Field(...)
    company: str = Field(...)
    phoneNumber: str = Field(...)
    birthDate: str = Field(...)
    address: str = Field(...)
    email: EmailStr = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "givenNames": "Carlos David",
                "lastName1": "Flores",
                "lastName2": "Silva",
                "position": "Developer",
                "company": "Own company",
                "phoneNumber": "3309876512",
                "birthDate": "18/09/1997",
                "email": "carloscode97@gmail.com",
                "address": "calle,num,colonia,ciudad,estado,CP",
            }
        }
        
class UpdatePersonModel(BaseModel):
    givenNames: Optional[str]
    email: Optional[EmailStr]
    lastName1: Optional[str]
    lastName2: Optional[str]
    position: Optional[str]
    company: Optional[str]
    phoneNumber: Optional[str]
    address: str = Field(...)
    birthDate: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "givenNames": "Carlos David",
                "lastName1": "Flores",
                "lastName2": "Silva",
                "position": "Developer",
                "company": "Own company",
                "phoneNumber": "3309876512",
                "birthDate": "18/09/1997",
                "email": "carloscode97@gmail.com",
                "address": "calle,num,colonia,ciudad,estado,CP",
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}