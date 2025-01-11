import requests
import json

api_url = 'https://jsonplaceholder.typicode.com/posts'

def function_api():
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            print(f"Status code: ", response.status_code)
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
x = function_api()
print(x)