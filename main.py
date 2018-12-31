from google.cloud import datastore
import uuid
import time

datastore_client = datastore.Client()
datastore_kind = 'Todos'


def helloWorld(request):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    resp = '{"todos": [{"name": "apple", "number": 6}, {"name": "cherry", "number": "1LB"}]}'
    return (resp, 200, headers)


def addTodo(request):
    request_json = request.get_json()
    todo_key = datastore_client.key(datastore_kind, str(uuid.uuid4()))
    todo = datastore.Entity(key=todo_key)
    if 'name' in request_json:
        todo['name'] = request_json['name']
    if 'quantity' in request_json:
        todo['quantity'] = request_json['quantity']
    todo['updated'] = time.ctime()
    datastore_client.put(todo)


if __name__ == '__main__':
    helloWorld('')
    addTodo({'name': 'Apple', 'quantity': 4})
