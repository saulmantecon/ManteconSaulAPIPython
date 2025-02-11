from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session
from app.db import models
from app.db.database import get_db
from app.schemas import Reserva, UpdateReserva

router = APIRouter(
    prefix="/reserva",
    tags=["reservas"]
)

@router.get("/lista_reservas", response_model=List[Reserva])
def lista_reservas(db: session = Depends(get_db)):
    reservas = db.query(models.Reserva)
    return reservas

@router.get("/reserva/{id}")
def reserva(id: int, db: session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

@router.post("/crear_reserva")
def crear_reserva(reserva: Reserva, db: session = Depends(get_db) ):
    reserva = reserva.model_dump()
    nueva_reserva = models.Reserva(**reserva)
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    return nueva_reserva

@router.delete("/eliminar_reserva/{id}")
def eliminar_reserva(id: int, db: session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    db.delete(reserva)
    db.commit()
    return {"message": "Reserva eliminada"}

@router.patch("/actualizar_reserva/{id}")
def actualizar_reserva(id: int, update_reserva: UpdateReserva, db: session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    reserva.update(update_reserva.model_dump(exclude_unset=True))
    db.commit()
    db.refresh(reserva)
    return {"message": "Reserva actualizada"}
