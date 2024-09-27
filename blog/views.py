from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog(request):
    """
    A view to return the blog page.
    """
    
    posts = Blog.objects.all().order_by('-date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles,
        'paginator': paginator,
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