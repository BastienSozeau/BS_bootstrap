from django.shortcuts import render

from boot_rules.forms import CommentForm
from boot_rules.models import Post, Comment



def boot_rules_index(request):
    posts = Post.objects.filter(status=1).order_by('-id')
    context = {
        "posts": posts,
    }
    return render(request, "boot_rules_index.html", context)

def boot_rules_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "boot_rules_category.html", context)

def boot_rules_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "boot_rules_detail.html", context)
