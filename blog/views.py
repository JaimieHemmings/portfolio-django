from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    """
    A view to return the blog page.
    """
    # get latest 3 articles
    articles = Blog.objects.all().order_by('-date')[:3]
    context = {
        'articles': articles,
    }
    return render(request, 'blog/blog.html', context)


def article(request, slug):
    """
    A view to return the article page.
    """
    article = Blog.objects.get(slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'blog/article.html', context)