from google.cloud import datastore
import uuid
import time
import json

datastore_client = datastore.Client()
datastore_kind = 'Todos'


def helloWorld(request):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    query = datastore_client.query(kind=datastore_kind)
    resp = json.dumps(list(query.fetch()))
    return (resp, 200, headers)


def addTodo(request):
    request_json = request.get_json()
    id = str(uuid.uuid4())
    todo_key = datastore_client.key(datastore_kind, id)
    todo = datastore.Entity(key=todo_key)
    if 'name' in request_json:
        todo['name'] = request_json['name']
    if 'quantity' in request_json:
        todo['quantity'] = request_json['quantity']
    todo['updated'] = time.ctime()
    todo['id'] = id
    todo['done'] = False
    datastore_client.put(todo)


def finishTodo(request):
    request_json = request.get_json()
    todo_key = datastore_client.key(datastore_kind, request_json['id']
    todo=datastore_client.get(key=todo_key)
    todo['done']=True
    todo['updated']=time.ctime()
    datastore_client.put(todo)


if __name__ == '__main__':
    todo_key=datastore_client.key(
        datastore_kind, '0a59ec71-d119-4371-b16c-35e73e9b9bc9')
    todo=datastore_client.get(key=todo_key)
    print(todo)
