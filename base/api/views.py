import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from base.models import Player, Results, User


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        # '/api/token',
        # '/api/token/refresh',
        '/api/players',
        '/api/player/id',
        '/api/players/popularity',
        '/api/player/new'
    ]

    return Response(routes)

#GET
def getAllPlayers(request):
    students = Player.objects.all()
    return HttpResponse(students)

def getPlayerID(request):
    return HttpResponse("ID de l'étudiant")

def getOrderPlayersByPopularity(request):
    return HttpResponse("Classement des 2tudiants par popularité")

#POST
def newPlayer(request):
    request_body = json.loads(request.body.decode('utf-8'))
    pseudo = request_body["pseudo"]
    image = request_body["image"]
    elo = request_body["elo"]
    attack = request_body["attack"]
    creator_id = request_body["creator_id"]

    Player.objects.create(pseudo=pseudo, image=image, elo=elo, attack=attack, creator_id=creator_id)
    return HttpResponse("Nouveau Player")

def newUser(request):
    request_body = json.loads(request.body.decode('utf-8'))
    name = request_body["name"]
    password = request_body["password"]

    User.objects.create(name=name, password=password)
    return HttpResponse("Nouveau User")

def newResult(request):
    request_body = json.loads(request.body.decode('utf-8'))
    player1_id = request_body["player1_id"]
    player2_id = request_body["player2_id"]
    winner_id = request_body["winner_id"]

    Results.objects.create(player1_id=player1_id, player2_id=player2_id, winner_id=winner_id)
    return HttpResponse("Nouveau Result")