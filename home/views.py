from django.shortcuts import render
from blog.models import Blog
from contact.forms import ContactForm
from django.contrib import messages


def index(request):
    """
    View function for the home page.
    """
    # Get latest 3 articles
    articles = Blog.objects.order_by('-date')[:6]
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully.')
        else:
            messages.error(request, 'Error sending the message, please check for errors.')

    context = {
        'articles': articles,
        'form': form,
    }
    return render(request, 'home/index.html', context)