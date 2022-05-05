from django.db import models

class Game(models.Model):
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=16)
    
    #creating an instance for my classes
    #on_delete tells django how we want the items to be deleted that contain a fk
    # and allow us to delete across tables
    
    
    #Note Migration is creating the table
    
    # remember "Gamer" is in reference to the class of gamer created in the models