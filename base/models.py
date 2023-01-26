from django.db import models

class Player(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pseudo = models.CharField(max_length=30)
    image = models.TextField()
    elo = models.IntegerField() 
    attack = models.IntegerField()
    creator_id = models.IntegerField()

class User(models.Model):
  id = models.PositiveIntegerField(primary_key=True)
  name = models.CharField(max_length=30)
  password = models.CharField(max_length=30)

class Results(models.Model):
  player1_id = models.PositiveIntegerField()
  player2_id = models.PositiveIntegerField()
  winner_id = models.PositiveIntegerField()
