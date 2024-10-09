import requests

def test_update_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'  # Atualizando o post com ID 1
    payload = {
        'id': 1,
        'title': 'updated title',
        'body': 'updated body',
        'userId': 1
    }

    # Fazendo a solicitação PUT para atualizar o post
    response = requests.put(url, json=payload)

    # Valida o status code da resposta
    assert response.status_code == 200

    # Valida se o título e o corpo no retorno são iguais aos enviados
    response_json = response.json()
    assert response_json['title'] == 'updated title'
    assert response_json['body'] == 'updated body'
    assert response_json['id'] == 1  # Verifica se o ID ainda é 1
