from django.urls import path
 
from . import views
 
urlpatterns = [
    path('helloapi', views.hello, name='hello'),
    path('blogPage', views.blogPage, name='bolgPage'),
    path('articalPage', views.articalPage, name="articlePage")
]