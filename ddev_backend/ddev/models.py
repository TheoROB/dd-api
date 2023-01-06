from django.db import models

# Create your models here.
class Player(models.Model):
    pseudo = models.CharField(max_length=50, null=False)
    image = models.ImageField()
    popularity = models.PositiveBigIntegerField(null=False)
    attack = models.PositiveBigIntegerField(null=False)
    defense = models.PositiveBigIntegerField(null=False)
    creator = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    pseudo = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)

class Result(models.Model):
    player1 = models.ForeignKey('Player', related_name='player1', on_delete=models.CASCADE, null=False)
    player2 = models.ForeignKey('Player', related_name='player2', on_delete=models.CASCADE, null=False)
    winner = models.ForeignKey('Player', on_delete=models.CASCADE, null=False)