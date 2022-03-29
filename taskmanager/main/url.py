from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('kindergarten', views.kindergarten, name='kindergarten'),
    path('school', views.school, name='school'),
    path('lyceum', views.lyceum, name='lyceum'),
    path('religion', views.religion, name='religion'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('news', views.news, name='news'),
    path('contacts', views.contacts, name='contacts')
]
