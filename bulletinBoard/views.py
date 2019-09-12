from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone
from django.urls import reverse
from .forms import CommentForm, BoardForm

from .models import Board, Comment

"""
本によると、まずは基本汎用ビューを用いて作ってみようとのことなので作ってみます
"""

class BoardIndexView(View):
    '''
    掲示板の一覧を表示するViewになる（予定）
    '''

    def get(self, request, *args, **kwargs):
        '''
        GETリクエスト用のメソッド
        *argsと**kwargsを引数にとるが、こいつらの存在意義がよくわかっていない。
        リクエスト以外でのデータや文字列の受け取りが発生する・・・？
        '''
        form = BoardForm(request.POST)
        context = {
            'form': form,
            'latest_board_list': Board.objects.all().order_by('pub_date'),
        }

        return render(request, 'bulletinBoard/index.html', context)

    def post(self, request, *args, **kwargs):
        '''
        POSTリクエスト用のメソッド
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('bulletinBoard:index',))


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
        current_board = get_object_or_404(Board, pk=board_id)
        comments = current_board.comment_set.all().order_by('remark_date')
        form = CommentForm(request.POST)
        context = {
            'board': current_board,
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
        current_board = get_object_or_404(Board, pk=board_id)
        new_instance = Comment(board=current_board)
        form = CommentForm(request.POST, instance=new_instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('bulletinBoard:detail', args=(board_id,)))

index = BoardIndexView.as_view()
detail = BoardDetailView.as_view()

# Create your views here.