'''
@Email: rumosky@163.com
@Author: rumosky
@Github: https://github.com/rumosky
@Date: 2020-06-29 16:17:34
@Description: urls
'''
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
