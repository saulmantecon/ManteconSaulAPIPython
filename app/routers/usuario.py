from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import Usuario, ShowUsuario,UpdateUsuario
from app.db.database import get_db
from sqlalchemy.orm import Session, session
from app.db import models

router = APIRouter(
    prefix="/usuario",
    tags=["usuarios"]
)

@router.get("/lista_usuarios", response_model=List[ShowUsuario])
def lista_usuarios(db: session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios

@router.get("/usuario/{id}", response_model=ShowUsuario)
def obtener_usuario(id: int, db: session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/crear_usuario")
def crear_usuario(usuario: Usuario, db: session = Depends(get_db)):
    usuario = usuario.model_dump()
    nuevo_usuario = models.Usuario(**usuario)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.delete("/eliminar_usuario/{id}")
def eliminar_usuario(id: int, db: session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"message": "Usuario eliminado"}

@router.patch("/actualizar_usuario/{id}")
def actualizar_usuario(id: int, update_usuario: UpdateUsuario, db: session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.update(update_usuario.model_dump(exclude_unset= True))
    db.commit()
    db.refresh(usuario)
    return {"message": "Usuario actualizado"}
