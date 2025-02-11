from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, DateTime
from datetime import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    contrasena = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(15))

    # Relación con Reservas
    reservas = relationship("Reserva", backref="Usuario", cascade="all, delete")


class Pista(Base):
    __tablename__ = 'pistas'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    tipo = Column(String(100), nullable=False)
    precio_hora = Column(DECIMAL(5, 2), nullable=False)

    # Relación con Reservas
    reservas = relationship("Reserva", backref="Pista", cascade="all, delete")

class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    id_pista = Column(Integer, ForeignKey('pistas.id', ondelete='CASCADE'), nullable=False)
    fecha_hora = Column(DateTime, default=datetime.now,onupdate=datetime.now)
    finalizada = Column(Boolean, default=False)