from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100)
    passsword=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name