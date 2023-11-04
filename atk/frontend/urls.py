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
    path('closelist/', views.closelist, name="closelist")
]