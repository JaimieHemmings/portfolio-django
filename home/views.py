from django.shortcuts import render

def index(request):
    """
    View function for the home page.
    """
    return render(request, 'home/index.html')


def growth_tips(request):
    """
    View function for the growth tips page.
    """
    return render(request, 'growth_tips/growth-tips.html')
