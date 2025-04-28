# Microsservice_Ecommerce

📚 Catálogo de Livros - Microsserviço

Este projeto é um microsserviço para catálogo de produtos (livros), desenvolvido com FastAPI, rodando em Docker.Ideal para aplicações que precisam de uma estrutura simples e escalável para gerenciar registros de livros.

🛠️ Tecnologias Utilizadas

FastAPI — Framework moderno para APIs com Python

Uvicorn — Servidor ASGI rápido para FastAPI

SQLAlchemy — ORM para interação com banco de dados

PostgreSQL — Banco de dados relacional (planejado ou opcional)

Docker — Contênirização da aplicação

Docker Compose — Orquestração de múltiplos serviços

📄 Descrição do Projeto

Este microsserviço permite:

Cadastrar livros

Listar livros cadastrados

Consultar detalhes de um livro por ID

Atualizar informações de livros

Deletar livros

Toda a comunicação é feita via API REST.A aplicação está pronta para rodar em ambientes containerizados usando Docker, facilitando deploys e escalabilidade.

🚀 Como Rodar o Projeto

Pré-requisitos

Docker instalado na sua máquina

Docker Compose (geralmente já vem com o Docker Desktop)

Passos para rodar o microsserviço:

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/backend/catalog

Suba o serviço com Docker Compose:

docker compose up --build

Este comando irá:

Construir a imagem do microsserviço

Rodar o contêiner

Acesse a aplicação:

A API estará disponível em: http://localhost:8000

A documentação automática (Swagger UI) estará em: http://localhost:8000/docs

🐳 Estrutura de Diretórios

backend/
└── catalog/
    ├── app/
    │   ├── main.py
    │   ├── models.py
    │   ├── routers/
    │   ├── schemas.py
    │   └── database.py
    ├── Dockerfile
    └── docker-compose.yml

⚙️ Comandos Útéis

Parar os contêineres:

docker compose down

Ver logs:

docker compose logs -f

Acessar o terminal do contêiner:

docker exec -it flask_micro-catalog-1 /bin/bash

📌 Notas Importantes

Arquivos estáticos: não são utilizados neste projeto, portanto o mount de diretórios foi removido.

Banco de dados: o exemplo atual pode utilizar SQLite em memória ou PostgreSQL, dependendo da configuração.
