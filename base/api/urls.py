from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    #get
    path('', views.getRoutes),
    path('players', views.getAllPlayers),
    path('player', views.getPlayerByID),
    path('players/elo', views.getOrderPlayersByElo),
    path('players/historical', views.getHistorical),
    path('player/historical', views.getHistoricalByID),
    #post
    path('player/new', views.newPlayer),
    path('user/new', views.newUser),
    path('result/new', views.newResult),
    #update
    path('player/update', views.updatePlayer),
    #delete
    path('player/delete', views.deletePlayerByID),
    path('user/delete', views.deleteUserByID),
]