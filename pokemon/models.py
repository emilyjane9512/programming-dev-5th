from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    place = models.CharField(max_length = 100)

class Pokemon(models.Model):
    name = models.CharField(max_length = 30)
    master = models.ForeignKey(User,blank=True, null=True)
    place = models.CharField(max_length = 100)

class Capture(models.Model):
    place = models.CharField(max_length = 100)
    master = models.ForeignKey(User)
    pokemon = models.OneToOneField(Pokemon)
    captured_at = models.DateTimeField(auto_now_add = True)

    #models.DateTimeField(default = timezone.now)