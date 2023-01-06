from django.contrib import admin
from ddev.models import *

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    
    list_display = ('pseudo', 'image', 'popularity', 'attack', 'defense', 'creator')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    list_display = ('pseudo', 'password')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    
    list_display = ('player1', 'player2', 'winner')
