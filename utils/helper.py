import json

def getJson(request):
    return json.loads(request.body.decode('utf-8'))