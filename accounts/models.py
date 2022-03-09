from django.db import models

# Create your models here.
class CreateUser(models.Model):
    class TYPE(models.TextChoices):
        Influencer = 'Influencer'
        Manufacture = 'Manufacture'
        Sponsor = 'Sponsor'
    username = models.CharField(max_length=20)
    Instagram = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    type = models.CharField(max_length=11, choices=TYPE.choices, default=TYPE.Influencer)
    def __str__(self):
        return self.username