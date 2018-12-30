from google.cloud import datastore
import uuid


def helloWorld(request):
    datastore_client = datastore.Client()
    kind = 'Todos'
    todo_key = datastore_client.key(kind, str(uuid.uuid4()))
    todo = datastore.Entity(key=todo_key)
    todo['name'] = 'Apple'
    datastore_client.put(todo)
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    resp = '{"todos": [{"name": "apple", "number": 6}, {"name": "cherry", "number": "1LB"}]}'
    return (resp, 200, headers)


if __name__ == '__main__':
    helloWorld('')
