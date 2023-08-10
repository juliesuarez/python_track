from django.urls import path
from myapp2 import views
urlpatterns = [
    path('index2/',views.index2,name='index2'),
    path('about/',views.about,name='about')
]