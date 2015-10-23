from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)

    def __str__(self):
        return "{} Age: {} Gender: {}".format(self.user.username, self.age,self.gender)