def helloWorld(request):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    resp = '{"todos": [{"name": "apple", "number": 6}, {"name": "cherry", "number": "1LB"}]}'
    return (resp, 200, headers)
