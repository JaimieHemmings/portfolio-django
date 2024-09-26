from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('growth-tips/', views.growth_tips, name='growth-tips'),
]