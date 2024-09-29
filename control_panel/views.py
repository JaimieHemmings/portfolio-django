from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from contact.models import Contact
from django.contrib.auth.models import User
from blog.models import Blog

# Check is superuser
@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):

    latest_messages = Contact.objects.all()[:5]
    total_unread_messages = Contact.objects.filter(read=False).count()
    total_num_users = User.objects.all().count()
    total_articles = Blog.objects.all().count()

    context = {
        'latest_messages': latest_messages,
        'total_unread_messages': total_unread_messages,
        'total_num_users': total_num_users,
        'total_articles': total_articles,

    }
    return render(request, 'control_panel/control-panel.html', context)


@user_passes_test(lambda u: u.is_superuser)
def toggle_message_read(request, message_id):
    message = Contact.objects.get(id=message_id)
    message.read = not message.read
    message.save()
    return redirect('view_messages')


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
    return render(request, 'control_panel/view-messages.html', context)


@user_passes_test(lambda u: u.is_superuser)
def view_message(request, message_id):
    all_messages = Contact.objects.all()
    latest_messages = Contact.objects.all()[:5]
    total_unread_messages = Contact.objects.filter(read=False).count()
    message = Contact.objects.get(id=message_id)
    context = {
        'message': message,
        'all_messages': all_messages,
        'latest_messages': latest_messages,
        'total_unread_messages': total_unread_messages,
    }
    return render(request, 'control_panel/view-message.html', context)
