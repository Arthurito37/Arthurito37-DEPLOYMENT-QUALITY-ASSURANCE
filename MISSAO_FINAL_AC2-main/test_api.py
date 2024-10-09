import requests

# Teste para verificar se a API responde corretamente
def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Verifica se o status code é 200
    assert response.status_code == 200  # Alterado de 2001 para 200

    # Verifica se a resposta é um JSON
    data = response.json()
    assert isinstance(data, list)

    # Verifica se há dados no JSON
    assert len(data) > 0

    # Verifica se os objetos contêm a chave 'userId'
    assert "userId" in data[0]
