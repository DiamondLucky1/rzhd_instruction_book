from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.ShowTopicTests.as_view(), name='test_topic'),
    path('test/<int:topic_id>/', views.ChoiceTopic.as_view(), name='test'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]