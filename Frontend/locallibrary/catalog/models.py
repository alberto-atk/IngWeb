from django.db import models

# Create your models here.
class Client(models.Model):
    """Model representing a book genre."""
    username = models.CharField(max_length=20, help_text="Username", primary_key=True,default='')
    
    name = models.CharField(max_length=15, help_text='Nombre')
    surname = models.CharField(max_length=30, help_text='Nombre')

    mail = models.EmailField(max_length=30, help_text="Email address")



    def __str__(self):
        """String for representing the Model object."""
        return self.username

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, help_text='Nombre')
    surname = models.CharField(max_length=30, help_text='Nombre')
    mail = models.EmailField(max_length=30, help_text="Email address")

    image = models.ImageField(max_length=100)
    description = models.CharField(max_length=500, help_text='Description')
    
    titles = models.CharField(max_length=500, help_text='Titles (comma separated)')
    collaborations = models.CharField(max_length=500, help_text='Collaborations(comma separated)')
    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)

