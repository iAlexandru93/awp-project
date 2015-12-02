from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from socialapp.models import UserPost,UserPostComment
from socialapp.forms import UserPostForm,CommentForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.order_by('-date_added')
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text)
            user_post.save()
        return redirect('index')


def post_details(request, pk):
    if request.method == 'GET':
        post = UserPost.objects.get(pk=pk)
        form = CommentForm()
        comments = UserPostComment.objects.filter(post=pk)
        context = {
            'post': post,
            'form': form,
            'comments':comments,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_comment = UserPostComment(text=text,post=UserPost.objects.get(pk=pk))
            user_comment.save()
        return redirect('post_details',pk)
    
