from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/new/', PostApiCreateView.as_view(), name='api-new'),
    path('blogs/', PostApiView.as_view()),
    path('blogs/<str:username>/', UserPostsAPIView.as_view()),
    path('blogs/<int:pk>', PostUpdateRetriveDelteView.as_view())
]