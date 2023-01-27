import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from base.models import Player, Results, User
from utils.helper import getJson
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/players',
        '/api/player/id',
        '/api/player/new',
        '/api/players/popularity',
        '/api/players/historical',
        '/api/players/historical/id'
    ]

    return Response(routes)


# GET /api/students
def getAllPlayers(request):
    students = Player.objects.all()
    return HttpResponse(students)


# GET /api/player/id
def getPlayerByID(request):
    request_body = getJson(request)
    id = request_body["id"]

    player = Player.objects.get(id=id)
    return HttpResponse(player)


# GET /api/players/elo
def getOrderPlayersByElo(request):
    players = Player.objects.all().order_by('elo').values()
    return HttpResponse(players)


# GET/api/players/historical
def getHistorical(request):
    historical = Results.objects.all()[:10]
    return HttpResponse(historical)


# GET /api/players/historical/id
def getHistorical(request):
    request_body = getJson(request)
    id = request_body["id"]
    histo1 = Results.objects.filter(player1_id=id)
    histo2 = Results.objects.filter(player2_id=id)

    historical = histo1 + histo2
    return HttpResponse(historical)


@csrf_exempt
# POST /api/player/new
def newPlayer(request):
    request_body = getJson(request)
    pseudo = request_body["pseudo"]
    image = request_body["image"]
    elo = request_body["elo"]
    attack = request_body["attack"]
    creator_id = request_body["creator_id"]

    Player.objects.create(pseudo=pseudo, image=image, elo=elo, attack=attack, creator_id=creator_id)
    return HttpResponse("Nouveau Player")


@csrf_exempt
# POST /api/user/new
def newUser(request):
    request_body = getJson(request)
    name = request_body["name"]
    password = request_body["password"]

    User.objects.create(name=name, password=password)
    return HttpResponse("Nouveau User")


@csrf_exempt
# POST /api/result/new
def newResult(request):
    request_body = getJson(request)
    player1_id = request_body["player1_id"]
    player2_id = request_body["player2_id"]
    winner_id = request_body["winner_id"]

    Results.objects.create(player1_id=player1_id, player2_id=player2_id, winner_id=winner_id)
    return HttpResponse("Nouveau Result")


@csrf_exempt
# POST /api/players/update/id
def updatePlayer(request):
    request_body = getJson(request)
    pseudo = request_body["pseudo"]
    image = request_body["image"]
    elo = request_body["elo"]
    attack = request_body["attack"]
    creator_id = request_body["creator_id"]

    Player.objects.update(pseudo=pseudo, image=image, elo=elo, attack=attack, creator_id=creator_id)
    return HttpResponse("Nouveau Result")


# DELETE /api/player
def deletePlayerByID(request):
    request_body = getJson(request)
    id = request_body["id"]

    Player.objects.filter(id=id).delete()
    return HttpResponse("Player deleted")


# DELETE /api/user
def deleteUserByID(request):
    request_body = getJson(request)
    id = request_body["id"]
    
    User.objects.filter(id=id).delete()
    return HttpResponse("User deleted")
