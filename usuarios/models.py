'''from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    
    email = models.EmailField()
    #first_name = models.CharField(max_length)
    #last_name = models.CharField(max_length)



    def __str__(self):
        return self.email'''