from django.shortcuts import render
from blog.models import Blog

def index(request):
    """
    View function for the home page.
    """
    # Get latest 3 articles
    articles = Blog.objects.order_by('-date')[:6]
    context = {
        'articles': articles,
    }
    return render(request, 'home/index.html', context)