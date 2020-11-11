from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def main_page(request):
    return render(request, 'blog/main_page.html', {})


def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__contains=search_query))
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # сохраняем данные формы без автора
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def contact_us(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        send_mail('test_mail',
                  message,
                  settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=False)
        return redirect('thank')
    return render(request, 'blog/contact_page.html')


def thanks_contact(request):
    return render(request, 'blog/thanks_for_contact.html')
