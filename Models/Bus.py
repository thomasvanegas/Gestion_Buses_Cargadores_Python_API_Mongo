# Importacion de Paquetes
from pydantic import BaseModel
from typing import Optional # Permite definir un atributo como nulleable

# Definicion del modelo -> Todos los modelos heredan de la clase BaseModel
class Bus(BaseModel):
    id: int
    placa: str
    marca: str
    estado: str
    ult_hora_carga: int