from . import views
from django.urls import path

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('kindergarten', views.kindergarten, name='kindergarten'),
    path('school', views.school, name='school'),
    path('lyceum', views.lyceum, name='lyceum'),
    path('religion', views.religion, name='religion'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('contacts', views.contacts, name='contacts')
]
