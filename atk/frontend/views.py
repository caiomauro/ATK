from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import ForumPost

# Create your views here.
@login_required
def home(request, *args, **kwargs):
    return render(request, 'frontend/home.html')

def login(request, *args, **kwargs):
    return render(request, 'frontend/login.html')

def auth(request, *args, **kwargs):
    return render(request, 'frontend/auth.html')

@login_required
def createpost(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        creator = request.user
        new_post = ForumPost.objects.create(title=title, content=content, creator=creator)
        new_post.save()
        return redirect('/home')
    return render(request, 'frontend/createpost.html')