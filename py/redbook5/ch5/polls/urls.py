from django.urls import path
from . import views

app_name = 'polls'
"""urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]"""
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),

    # /polls/99/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /poll/99/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /poll/99/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]