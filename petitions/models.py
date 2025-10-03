from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Votes(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.votes