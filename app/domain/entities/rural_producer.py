from typing import Optional
from pydantic import BaseModel, condecimal


class RuralProducer(BaseModel):
    id: Optional[int] = None
    documento_tipo: Optional[str] = None
    documento_numero: Optional[str] = None
    nome_produtor: Optional[str] = None
    nome_fazenda: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    area_total_hectares: Optional[condecimal(max_digits=10, decimal_places=2, ge=0)] = None
    area_agricultavel_hectares: Optional[condecimal(max_digits=10, decimal_places=2, ge=0)] = None
    area_vegetacao_hectares: Optional[condecimal(max_digits=10, decimal_places=2, ge=0)] = None
    culturas_plantadas: Optional[str] = None

    class Config:
        from_attributes = True

