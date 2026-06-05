import requests

# Endpoint fornecido pela plataforma JSONPlaceholder para testes de API
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print(response.json())
# Retorna HTTP 200: Bem-Sucedido
print(response.status_code)
print(response.headers["Content-Type"])