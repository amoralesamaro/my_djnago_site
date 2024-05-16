from django.shortcuts import render
from django.utils import timezone
from .models import Article
from django.shortcuts import render, get_object_or_404

# Create your views here.


def post_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "article/post_list.html", {"articles": articles})


def post_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article/post_detail.html", {"article": article})
