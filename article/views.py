from django.utils import timezone
from .models import Article
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

# Create your views here.


def post_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "article/post_list.html", {"articles": articles})


def post_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article/post_detail.html", {"article": article})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect("post_detail", pk=article.pk)
    else:
        form = PostForm()
    return render(request, "article/post_edit.html", {"form": form})


def post_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect("post_detail", pk=article.pk)
    else:
        form = PostForm(instance=article)
    return render(request, "article/post_edit.html", {"form": form})
