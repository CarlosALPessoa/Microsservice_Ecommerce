from pydantic import BaseModel, ConfigDict 

class LivroCreate(BaseModel):
    titulo: str
    descricao: str
    preco: float
    image: str

class LivroResponse(LivroCreate):
    id: int

    
model_config = ConfigDict(
        from_attributes=True, 
        populate_by_name=True 
    )
