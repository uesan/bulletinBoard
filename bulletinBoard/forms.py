from django import forms
from .models import Board, Comment
from django.shortcuts import get_object_or_404
from django.utils import timezone

class CommentForm(forms.Form):
    '''
    コメント投稿用フォーム
    '''
    board_id = 0
    text = forms.CharField(
        label='コメント本文',
    )

    def clean(self):
        new_text = self.cleaned_data.get('text')
        print(new_text)
        try:
            print(new_text)
            board = get_object_or_404(Board, pk=self.board_id)
            board.comment_set.create(text=new_text, remark_date=timezone.now())
            #new_comment = Comment(text=new_text, remark_date=timezone.now(),)
            print(board)
            #new_comment.save()

        except:
            raise forms.ValidationError("コメント投稿できませんでした")

