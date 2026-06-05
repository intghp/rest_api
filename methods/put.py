import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

print("---------------------------------------------------------------")

todo = {"userId": 1, "title": "Wash car", "completed": True}
# Método utilizado para substituição
response = requests.put(api_url, json=todo)
print(response.json())

# Receberá HTTP 200 porque atualizando um existente, por isso não recebe 201
print(response.status_code)