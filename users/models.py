from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=12)
    picture = models.ImageField(upload_to='profile/', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email


