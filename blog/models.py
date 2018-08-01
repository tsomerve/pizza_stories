from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}: {self.author.first_name} {self.author.last_name}'