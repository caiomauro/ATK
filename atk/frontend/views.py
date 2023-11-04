from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from api.models import ForumPost

# Create your views here.
@login_required
def home(request, *args, **kwargs):
    if request.user.is_authenticated:
        forum_posts = ForumPost.objects.all()
        return render(request, 'frontend/home.html', {'forum_posts': forum_posts})
    else:
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

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        if request.user.is_staff:
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'You do not have permission to delete this post.')
            return redirect('home')
    return render(request, 'frontend/delete_post.html', {'post': post})