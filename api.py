import requests
import json
import boto3

api_url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(api_url)
attributes = dir(response)
print(attributes)

ec2_client = boto3.client('ec2')
attributes_ec2 = dir(ec2_client.run_instances)
print(attributes_ec2)
print(ec2_client.__str__)

def function_api():
    try:
        response = requests.get(api_url)
        print(response)
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