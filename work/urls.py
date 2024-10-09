from django.urls import path
from . import views

urlpatterns = [
  path("", views.work, name="work"),
  path("<slug:slug>/", views.work_detail, name="work_detail"),
]