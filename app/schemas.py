from datetime import datetime
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    contrasena: str
    apellido: str
    email: str
    telefono: str


class ShowUsuario(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str


class UpdateUsuario(BaseModel):
    nombre: str = None
    contrasena: str = None
    apellido: str = None
    email: str = None
    telefono: str = None

class Pista(BaseModel):
    nombre: str
    tipo: str
    precio_hora: float

class UpdatePista(BaseModel):
    nombre: str = None
    tipo: str = None
    precio_hora: float = None

class Reserva(BaseModel):
    id_usuario: int
    id_pista: int
    fecha_hora: datetime
    finalizada: bool = False
    model_config = {
        "from_attributes": True
    }

class UpdateReserva(BaseModel):
    id_usuario: int = None
    id_pista: int = None
    fecha_hora: datetime = None
    finalizada: bool = False
    model_config = {
        "from_attributes": True
    }




