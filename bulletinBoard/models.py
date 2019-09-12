from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,AnonymousUser

# Create your models here.

class Board(models.Model):
    '''
    掲示板の「板」にあたる部分のモデル。
    :parameter
    ----------
    title : django.db.models.CharField
        板のタイトル

    pub_date : django.db.models.DateTimeField
        チュートリアルと同じく、掲示される日時

    '''
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('dete published', default=timezone.now(), db_index=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    「板」につくコメントにあたるモデル
    :parameter
    ----------
    text : django.db.models.TextField
        コメント本文

    board : django.db.models.ForeignKey(this.Board)
        どの「板」のコメントかを判断する変数

    '''
    text = models.TextField(max_length=400)
    remark_date = models.DateTimeField('date remarked', default=timezone.now(), db_index=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.text