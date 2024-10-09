import requests
import urllib3

# Suprimir avisos de InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_delete_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'  # Deletando o post com ID 1

    # Fazendo a solicitação DELETE para remover o post
    response = requests.delete(url, verify=False)

    # Valida se a resposta é 200 (OK) ou 204 (Sem Conteúdo)
    assert response.status_code in [200, 204]

    # Verifica se o post foi realmente excluído tentando obtê-lo
    get_response = requests.get(url)
    # Espera-se que o post ainda seja encontrado, então espera-se 200
    assert get_response.status_code == 200  # O post ainda pode estar acessível
