from django.shortcuts import render


def services(request):
    return render(request, 'services/services.html')


def web_design(request):
    return render(request, 'services/web-design.html')


def search_engine_optimisation(request):
    return render(request, 'services/seo.html')


def copywriting(request):
    return render(request, 'services/copywriting.html')