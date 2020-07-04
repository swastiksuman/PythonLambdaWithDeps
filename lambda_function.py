import requests


def lambda_handler(event, context):
    response = requests.get("https://reqres.in/api/users?page=2")
    return response.json()
