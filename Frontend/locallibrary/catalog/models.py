from django.db import models

# Create your models here.
class User(models.Model):
    """Model representing a book genre."""
    login = models.CharField(max_length=20, help_text="Username", primary_key=True,default='')
    
    name = models.CharField(max_length=15, help_text='Nombre')
    surname = models.CharField(max_length=30, help_text='Nombre')

    mail = models.EmailField(max_length=30, help_text="Email address")
    password = models.CharField(max_length=15, help_text='pass')



    def __str__(self):
        """String for representing the Model object."""
        return self.username