from itertools import chain
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from base.models import Player, Results, User
from utils.helper import getJson, toJson
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def getRoutes(request):
    routes = [
        #post
        'players/',
        'player/',
        'players/elo/',
        'players/historical/',
        'player/historical/',
        #post
        'player/new/'
        'user/new/',
        'result/new/',
        #update
        'player/update/',
        #delete
        'player/delete/',
        'user/delete/',
    ]

    return Response(routes)


# GET /api/players
def getAllPlayers(request):
    players = Player.objects.all()
    return HttpResponse(players.values())


# GET /api/player
def getPlayerByID(request):
    request_body = getJson(request)
    id = request_body["id"]

    player = Player.objects.get(id=id)
    return HttpResponse(player.values())


# GET /api/players/elo
def getOrderPlayersByElo(request):
    players = Player.objects.all().order_by('elo').values()
    return HttpResponse(players.values())


# GET/api/players/historical
def getHistorical(request):
    historical = Results.objects.all()[:9]
    return HttpResponse(historical.values())


# GET /api/player/historical
def getHistoricalByID(request):
    request_body = getJson(request)
    id = request_body["id"]
    histo1 = Results.objects.filter(player1_id=id)
    histo2 = Results.objects.filter(player2_id=id)

    historical = len(list(chain(histo1, histo2)))
    return HttpResponse(historical.values())


@csrf_exempt
# POST /api/player/new
def newPlayer(request):
    request_body = getJson(request)
    pseudo = request_body["pseudo"]
    image = request_body["image"]
    elo = request_body["elo"]
    attack = request_body["attack"]
    creator_id = User.objects.get(id=request_body["creator_id"])

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
    player1_id = Player.objects.get(id=request_body["player1_id"])
    player2_id = Player.objects.get(id=request_body["player2_id"])
    winner_id = Player.objects.get(id=request_body["winner_id"])

    Results.objects.create(player1_id=player1_id, player2_id=player2_id, winner_id=winner_id)
    return HttpResponse("Nouveau Result")


@csrf_exempt
# PUT /api/players/update
def updatePlayer(request):
    request_body = getJson(request)
    id = request_body["id"]
    pseudo = request_body["pseudo"]
    image = request_body["image"]
    elo = request_body["elo"]
    attack = request_body["attack"]
    creator_id = request_body["creator_id"]

    Player.objects.filter(pk=id).update(pseudo=pseudo, image=image, elo=elo, attack=attack, creator_id=creator_id)
    return HttpResponse("Nouveau Result")


# DELETE /api/player/delete
@csrf_exempt
def deletePlayerByID(request):
    request_body = getJson(request)
    id = request_body["id"]

    Player.objects.filter(pk=id).delete()
    return HttpResponse("Player deleted")


# DELETE /api/user/delete
@csrf_exempt
def deleteUserByID(request):
    request_body = getJson(request)
    id = request_body["id"]
    
    User.objects.filter(pk=id).delete()
    return HttpResponse("User deleted")
