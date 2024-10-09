from django.shortcuts import render
from .models import PortfolioItem
from django.core.paginator import Paginator


def work(request):
    """
    View function for the home page.
    """
    portfolio_items = PortfolioItem.objects.all()
    paginator = Paginator(portfolio_items, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'portfolio_items': portfolio_items,
        "articles": articles,
    }
    return render(request, 'work/work.html', context)
