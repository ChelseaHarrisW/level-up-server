from django.db import models

class Event_gamer(models.Model):
    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE )
    event = models.ForeignKey("event", on_delete=models.CASCADE )
    
    #No need for this because the many to mant field has been declaired on the Event model