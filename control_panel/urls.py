from django.urls import path
from . import views

urlpatterns = [
  path('', views.control_panel, name='control_panel'),
  path('messages/toggle_message_read/<int:message_id>/', views.toggle_message_read, name='toggle_message_read'),
  path('messages/', views.view_messages, name='view_messages'),
  path('messages/<int:message_id>/', views.view_message, name='view_message'),
]