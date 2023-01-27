import json

from django.forms import model_to_dict

from django.core  import serializers

def getJson(request):
    return json.loads(request.body.decode('utf-8'))

def toJson(object):
    dict_obj = model_to_dict( object )

    data = json.dumps(dict_obj)
    return data
