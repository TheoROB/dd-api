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
    path('player/id/', views.getPlayerID),
    path('players/popularity', views.getOrderPlayersByPopularity),
    #post
    path('player/new', views.newPlayer),
    path('user/new', views.newUser),
    path('result/new', views.newResult),

    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]