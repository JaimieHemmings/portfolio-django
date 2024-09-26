from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    """
    View function for the home page.
    """
    context = {}
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully.')
        else:
            messages.error(request, 'Error sending the message, please check for errors.')

    context['form'] = form
    return render(request, 'contact/contact.html', context)