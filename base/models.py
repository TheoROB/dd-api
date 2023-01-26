from django.db import models

class User(models.Model):
  id = models.AutoField(primary_key=True, editable=False)
  name = models.CharField(max_length=30)
  password = models.CharField(max_length=30)

class Player(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    pseudo = models.CharField(max_length=30)
    image = models.TextField()
    elo = models.IntegerField() 
    attack = models.IntegerField()
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="re_creator_id")

class Results(models.Model):
  id = models.AutoField(primary_key=True, editable=False)
  player1_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="re_player1_id")
  player2_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="re_player2_id")
  winner_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="re_winner_id")
