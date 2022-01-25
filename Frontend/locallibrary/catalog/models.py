from django.db import models

# Create your models here.

class User(models.Model):
    #Fields
    login = models.CharField(max_length=20, help_text="Username", primary_key=True,default='')
    mail = models.EmailField(max_length=30, help_text="Email address")
    userType = models.CharField(max_length=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.login


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    user = models.ForeignKey('User',on_delete=models.CASCADE)


