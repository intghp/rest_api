import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}

# Patch: Substitui apenas valores definidos no Json
response = requests.patch(api_url, json=todo)
print(response.json())

# HTTP 200
print(response.status_code)