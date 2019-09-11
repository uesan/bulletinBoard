from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone
from .forms import CommentForm, BoardForm

from .models import Board, Comment

"""
本によると、まずは基本汎用ビューを用いて作ってみようとのことなので作ってみます
"""

class BoardIndexView(View):
    '''
    掲示板の一覧を表示するViewになる（予定）
    '''
    #context_object_name = 'latest_board_list'
    context = {
        'latest_board_list': Board.objects.all()
    }

    def get(self, request, *args, **kwargs):
        '''
        GETリクエスト用のメソッド
        *argsと**kwargsを引数にとるが、こいつらの存在意義がよくわかっていない。
        リクエスト以外でのデータや文字列の受け取りが発生する・・・？
        '''
        form = BoardForm(request.POST)
        context = {
            'form': form,
            'latest_board_list': Board.objects.all(),
        }

        return render(request, 'bulletinBoard/index.html', self.context)

class BoardDetailView(View):
    '''
    掲示板の実際の内容について表示するView
    '''
    context = {
        'board': Board.objects.all()
    }
    def get(self, request, board_id, *args, **kwargs):
        '''
        GETリクエスト用のメソッド
        *argsと**kwargsを引数にとるが、こいつらの存在意義がよくわかっていない。
        リクエスト以外でのデータや文字列の受け取りが発生する・・・？
        '''
        board = get_object_or_404(Board, pk=board_id)
        comments = board.comment_set.all().order_by('remark_date')
        form = CommentForm(request.POST)
        form.board_id = board_id
        context = {
            'board': board,
            'comments': comments,
            'form': form,
        }
        return render(request, 'bulletinBoard/detail.html', context)

    def post(self, request, board_id, *args, **kwargs):
        '''

        :param request:
        :param board_id:
        :param args:
        :param kwargs:
        :return:
        '''
        form = CommentForm(request.POST)
        new_comment = form.save()
        board = get_object_or_404(Board, pk=board_id)
        comments = board.comment_set.all().order_by('remark_date')
        context = {
            'board': board,
            'comments': comments,
            'form': form,
        }
        return render(request, 'bulletinBoard/detail.html', context)

index = BoardIndexView.as_view()
detail = BoardDetailView.as_view()

# Create your views here.
