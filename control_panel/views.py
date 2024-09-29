from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from contact.models import Contact

# Check is superuser
@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):
    latest_messages = Contact.objects.all()[:5]
    total_unread_messages = Contact.objects.filter(read=False).count()
    context = {
        'latest_messages': latest_messages,
        'total_unread_messages': total_unread_messages
    }
    return render(request, 'control_panel/control_panel.html', context)


@user_passes_test(lambda u: u.is_superuser)
def toggle_message_read(request, message_id):
    message = Contact.objects.get(id=message_id)
    message.read = not message.read
    message.save()
    return redirect('control_panel')


@user_passes_test(lambda u: u.is_superuser)
def view_messages(request):
    all_messages = Contact.objects.all()
    latest_messages = Contact.objects.all()[:5]
    total_unread_messages = Contact.objects.filter(read=False).count()
    context = {
        'all_messages': all_messages,
        'latest_messages': latest_messages,
        'total_unread_messages': total_unread_messages,
    }
    return render(request, 'control_panel/view_messages.html', context)
