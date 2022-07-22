from django.db import models

# Create your models here.
class Profile(models.Model):
    passport = models.CharField(max_length=50)
    about = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=60)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    completion_date = models.DateField('date completed')
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.title

