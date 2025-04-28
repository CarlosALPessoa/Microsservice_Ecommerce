import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Fixture para carregar os dados dos livros
@pytest.fixture(scope="module")
def livros_data():
    with open('livros.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Fixture para criar livros temporários
@pytest.fixture(scope="module")
def created_livros_ids(livros_data):
    ids = []
    for livro in livros_data:
        response = client.post("/livros", json=livro)
        assert response.status_code in [200, 201], f"Falha ao criar livro: {livro['titulo']}"
        ids.append(response.json()["id"])
    return ids

def test_criacao_livros(created_livros_ids):
    """Testa a criação de livros e verifica se foram armazenados"""
    assert len(created_livros_ids) > 0, "Nenhum livro foi criado"
    
    # Verifica se os IDs são únicos
    unique_ids = set(created_livros_ids)
    assert len(unique_ids) == len(created_livros_ids), "IDs duplicados encontrados"

def test_consulta_livro_aleatorio(created_livros_ids):
    """Testa a consulta de um livro aleatório"""
    import random
    random_id = random.choice(created_livros_ids)
    
    response = client.get(f"/livros/{random_id}")
    assert response.status_code == 200, f"Falha ao consultar livro ID {random_id}"
    
    livro = response.json()
    assert "id" in livro, "Resposta não contém ID do livro"
    assert livro["id"] == random_id, "ID do livro não corresponde ao solicitado"

def test_estrutura_resposta_livro(created_livros_ids):
    """Verifica se a estrutura da resposta está correta"""
    response = client.get(f"/livros/{created_livros_ids[0]}")
    livro = response.json()
    
    campos_obrigatorios = {
        "id": int,
        "titulo": str,
        "descricao": str,
        "preco": float,
        "image": str
    }
    
    for campo, tipo in campos_obrigatorios.items():
        assert campo in livro, f"Campo obrigatório faltando: {campo}"
        assert isinstance(livro[campo], tipo), f"Tipo incorreto para {campo}. Esperado {tipo}, obtido {type(livro[campo])}"

# Teste adicional para caso de livro não encontrado
def test_consulta_livro_inexistente():
    response = client.get("/livros/999999")
    assert response.status_code == 404, "Deveria retornar 404 para livro não encontrado"
    assert "detail" in response.json(), "Resposta de erro deve conter 'detail'"