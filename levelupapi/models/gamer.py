from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)


# telling Django how  to interact with the gamer model aswell as what that means
# remimber: objects are made from the data pulled from the database
# #creating the table we are also creating tables here
#ORM is how we comunicate with the DB (through the model)


#Django provides the info for users but we need more info so we will associate this class with users