from django.shortcuts import render


def work(request):
    """
    View function for the home page.
    """
    return render(request, 'work/work.html')
