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
    path('players/', views.getAllPlayers),
    path('player/id/', views.getPlayerByID),
    path('players/popularity', views.getOrderPlayersByElo),
    #post
    path('player/new', views.newPlayer),
    path('user/new', views.newUser),
    path('result/new', views.newResult),
    path('players/elo', views.getOrderPlayersByElo),
]