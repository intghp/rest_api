import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
# HTTP 200: Operação bem-sucedida
print(response.status_code)