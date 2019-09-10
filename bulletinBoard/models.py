from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('dete published')

class comment(models.Model):
    text = models.TextField(max_length = 400)
    Board = models.ForeignKey(Board, on_delete = models.CASCADE)