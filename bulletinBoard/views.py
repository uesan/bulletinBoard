from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

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
        return render(request, 'bulletinBoard/index.html')

index = BoardIndexView.as_view()

# Create your views here.
