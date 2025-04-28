from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from models import Livro
import shutil, os
import schemas, models

router = APIRouter()

@router.get("/livros")
def listar_livros(db: Session = Depends(get_db)):
    return db.query(Livro).all()

@router.get("/livros/{id}")
def details_book(id: int, db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.id == id).first()

@router.post("/livros")
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    novo_livro = models.Livro(**livro.dict())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro