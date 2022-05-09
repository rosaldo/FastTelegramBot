#!/usr/bin/env python3
# coding: utf-8

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Ola": "Mundo"}


# Criar Model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str


# Criar Base de Dados
base_de_dados = [
    Usuario(id=1, email="primeiro@teste.com.br", senha="usupri123"),
    Usuario(id=2, email="segundo@teste.com.br", senha="ususec123"),
]

# Rota Get All
@app.get("/usuarios")
def get_todos_usuarios():
    return base_de_dados


# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if usuario.id == id_usuario:
            return usuario
    return {"Status": 404, "Mensagem": "Usuario nao encontrado"}


# Rota Insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # Criar regras de negocio
    base_de_dados.append(usuario)
    return usuario
