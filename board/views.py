from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def index(request):
    posts_list = Post.objects.all().order_by('-created_at') 
    paginator = Paginator(posts_list, 5)  # 5개씩 페이지 나눔
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'board/index.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = PostForm()

    return render(request, 'board/create_post.html', {'form': form})