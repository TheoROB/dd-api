import json

from django.forms import model_to_dict

from django.core  import serializers

def getJson(request):
    return json.loads(request.body.decode('utf-8'))

