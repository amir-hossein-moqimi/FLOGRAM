from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
# class CreateUser(models.Model):
#     class TYPE(models.TextChoices):
#         Influencer = 'Influencer'
#         Manufacture = 'Manufacture'
#         Sponsor = 'Sponsor'
#     username = models.CharField(max_length=50)
#     Instagram = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     type = models.CharField(max_length=11, choices=TYPE.choices, default=TYPE.Influencer)
#     def __str__(self):
#         return self.username
User._meta.get_field('email')._unique = True
User._meta.get_field('email')._blank = False

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class TYPE(models.TextChoices):
        Influencer = 'Influencer'
        Manufacture = 'Manufacture'
        Sponsor = 'Sponsor'
    Instagram = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=11, choices=TYPE.choices, default=TYPE.Influencer)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)