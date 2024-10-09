import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    # Verifica se o status code é 201 (Criado)
    assert response.status_code == 201

    # Verifica se o retorno contém o id do novo recurso
    data = response.json()
    assert "id" in data
