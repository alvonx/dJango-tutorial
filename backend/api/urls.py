from django.urls import path

from . import views


urlpatterns = [
    path('', views.api_home),  # localhost:8000/api
    path('query', views.api_query)  # localhost:8000/api/query
]