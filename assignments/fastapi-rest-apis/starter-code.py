from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# Armazene os dados em memória para o exercício
items = [
    {"id": 1, "name": "Sample item", "done": False},
]


class ItemCreate(BaseModel):
    name: str
    done: bool = False


class Item(ItemCreate):
    id: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI task API"}


@app.get("/items")
def list_items():
    # Retorne a lista completa de itens
    return items


@app.post("/items")
def create_item(item: ItemCreate):
    # Crie um novo item com um ID único e adicione à lista
    # Não esqueça de retornar o item criado com status 201
    raise NotImplementedError("Implement this endpoint")


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Busque um item por ID e retorne 404 se não existir
    raise NotImplementedError("Implement this endpoint")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    # Atualize o item existente e retorne o resultado atualizado
    raise NotImplementedError("Implement this endpoint")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Remova o item e retorne uma mensagem de confirmação
    raise NotImplementedError("Implement this endpoint")
