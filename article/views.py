from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here.


def post_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "article/post_list.html", {"articles": articles})
