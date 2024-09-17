from datetime import datetime
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "CRM"
    produto2 = "Midias Sociais"
    produto3 = "Trafego"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v
