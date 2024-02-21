from django.urls import path
from . import views

urlpatterns = [
    path('url1/',views.link1,name = 'link1'),
    
]