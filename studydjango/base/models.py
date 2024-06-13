from django.db import models
from django.contrib.auth.models import User
# from django.db.models.deletion import CASCADE
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # add one (topic) to many (Room) relationship
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # Many to many relationship 
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Set one (user) to many (message) relationship
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Set one (room) to many (message) relationship
    body = models.TextField()
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-update', '-created']
    def __str__(self) -> str:
        return self.body[0:20]
