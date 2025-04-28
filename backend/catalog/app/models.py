from sqlalchemy import Column, Integer, String, Float
from database import Base
from pydantic import BaseModel

class Livro(Base):
    __tablename__ = "Livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(50), index=True)
    descricao = Column(String(50))
    preco = Column(Float)
    image = Column(String)