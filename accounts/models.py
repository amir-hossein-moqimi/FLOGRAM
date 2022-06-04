from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class TYPE(models.TextChoices):
        Influencer = 'Influencer'
        Manufacture = 'Manufacture'
        Sponsor = 'Sponsor'
    Instagram = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=11, choices=TYPE.choices, default=TYPE.Influencer, null=True)
    email = models.EmailField(max_length=50, null=True)
    verified = models.BooleanField(default=False)
    description = models.CharField(max_length=1000, default='no description!') 
    money = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def generate_unique_code():
    characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    while True:
        code = ''.join(random.choices(characters, k=6))
        if Request_Code.objects.filter(code=code).count() == 0:
            break
    return code

class Request_Code(models.Model):
    code = models.CharField(max_length=6, default=generate_unique_code)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.code