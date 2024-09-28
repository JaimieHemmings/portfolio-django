from django.urls import path
from . import views

urlpatterns = [
  path('', views.services, name='services'),
  path('web-design', views.web_design, name='web_design'),
  path('search-engine-optimisation', views.search_engine_optimisation, name='search_engine_optimisation'),
  path('copywriting', views.copywriting, name='copywriting'),
]