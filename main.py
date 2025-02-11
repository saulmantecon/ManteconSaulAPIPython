from fastapi import FastAPI
import uvicorn
from app.routers import usuario, reserva,pista
from app.db.database import Base, engine

def create_tables():
 Base.metadata.create_all(bind=engine)

create_tables()


app = FastAPI()
app.include_router(usuario.router)
app.include_router(pista.router)
app.include_router(reserva.router)
