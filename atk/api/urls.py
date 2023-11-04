from django.urls import path
from .views import ForumPostListView

urlpatterns = [
    path('forum-posts/', ForumPostListView.as_view(), name='forum-post-list'),
]
