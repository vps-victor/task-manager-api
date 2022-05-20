from fastapi.testclient import TestClient
from fastapi import status
from task_manager.manager import app, TASKS


def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/task")
    assert resposta.status_code == status.HTTP_200_OK

def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/task")
    assert resposta.headers["Content-Type"] == "application/json"

def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/task")
    assert isinstance(resposta.json(), list)

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TASKS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "title 1",
            "description": "description 1",
            "status": "finished",
        }
    )
    cliente = TestClient(app)
    response = cliente.get("/task")
    assert "id" in response.json().pop()
    TASKS.clear()
