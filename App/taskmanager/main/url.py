from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('kindergarten', views.kindergarten, name='kindergarten'),
    path('school', views.school, name='school'),
    path('college', views.college, name='college'),
    path('religion', views.religion, name='religion'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('contacts', views.contacts, name='contacts')
]
