from django.urls import path

from . import views

app_name = 'bulletinBoard'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail')
]