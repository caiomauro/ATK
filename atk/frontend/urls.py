from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='frontend/login.html'), name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='frontend/login.html'), name="login"),
    path('home/', views.home, name="home"),
    path('createpost/', views.createpost, name="createpost"),
    path('deletepost/<int:post_id>/', views.delete_post, name='delete_post'),
    path('tools/', views.tools, name="tools"),
    path('closelist/', views.closelist, name="closelist"),
    path('markcomplete/<int:post_id>/', views.mark_complete, name='mark_complete'),
    path('completedtasks/', views.completed_tasks, name='completed_tasks'),
    path('markincomplete/<int:post_id>/', views.mark_incomplete, name='mark_incomplete'),
]