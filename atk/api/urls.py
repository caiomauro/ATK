from django.urls import path
from .views import userInfoView

urlpatterns = [
    path('data/', userInfoView.as_view()),
]