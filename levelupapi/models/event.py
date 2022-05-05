from django.db import models


class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", related_name="Gamers")

#Dropping the _id for game because Django is compairing the intire game not just the id field

#adding the gamer info for join table as attendees. THAT IS Your join table^^