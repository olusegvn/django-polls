from django.urls import path

from .views import *

app_name = 'polls'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', Detail.as_view(), name='detail'),
    path('<int:pk>/results/', Results.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]