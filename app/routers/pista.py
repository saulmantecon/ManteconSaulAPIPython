from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, session
from app.db import models
from app.db.database import get_db
from app.schemas import Pista, UpdatePista
router = APIRouter(
    prefix="/pista",
    tags=["pistas"]
)

@router.get("/lista_pistas")
def get_pistas(db: session = Depends(get_db)):
    pistas = db.query(models.Pista).all()
    return pistas

@router.get("/pista/{id}")
def get_pista(id: int, db: session = Depends(get_db)):
    pista = db.query(models.Pista).filter(models.Pista.id == id).first()
    if not pista:
        raise HTTPException(status_code=404, detail="Pista not found")
    return pista

@router.post("/crear_pista")
def crear_pista(pista: Pista, db: session = Depends(get_db)):
    pista = pista.model_dump()
    nueva_pista = models.Pista(**pista)
    db.add(nueva_pista)
    db.commit()
    db.refresh(nueva_pista)
    return nueva_pista

@router.delete("/eliminar_pista/{id}")
def eliminar_pista(id: int, db: session = Depends(get_db)):
    pista = db.query(models.Pista).filter(models.Pista.id == id).first()
    if not pista:
        raise HTTPException(status_code=404, detail="Pista not found")
    db.delete(pista)
    db.commit()
    return {"message": "Pista eliminada"}

@router.patch("/actualizar_pista/{id}")
def actualizar_pista(id: int, update_pista : UpdatePista, db: session = Depends(get_db)):
    pista = db.query(models.Pista).filter(models.Pista.id == id).first()
    if not pista:
        raise HTTPException(status_code=404, detail="Pista not found")
    pista.update(update_pista.model_dump(exclude_unset=True))
    db.commit()
    db.refresh(pista)
    return {"message": "Pista actualizada"}



