from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Post
from .forms import PostForm

from cv.models import Traits
from cv.forms import TraitsForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def cv_view(request):
    traits = Traits.objects.all()
    return render(request, '../../cv/templates/cv/cv.html', {'traits' : traits})

def cv_edit(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    if request.method == "POST":
        form = TraitsForm(request.POST, instance=trait)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('cv_view')
    else:
        form = TraitsForm(instance=trait) 
    return render(request, '../../cv/templates/cv/cv_edit.html', {'form': form})

def cv_new(request):
    if request.method == "POST":
        form = TraitsForm(request.POST)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('cv_view')
    else:
        form = TraitsForm()
    return render(request, '../../cv/templates/cv/cv_edit.html', {'form': form})

