from .models import Post
from datetime import date
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts' : posts
	}
	return render(request,'blog/post_list.html',context)


def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	context = {
		'post' : post
	}
	return render(request, 'blog/post_detail.html',context)


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = date.today()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:		
		form = PostForm()
	context = {
		'form' : form
	}
	return render(request, 'blog/post_edit.html',context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
    	'form' : form
    }
    return render(request, 'blog/post_edit.html', context)


def post_clap(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.claps += 1
    post.save()
    return redirect(reverse('blog:post_detail', kwargs={'pk':pk}))