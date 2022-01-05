from django.shortcuts import render
from .models import NewsDB


def news_home(request):
    news_obj = NewsDB.objects.order_by('id')
    return render(request, 'main/news.html', {'news_obj': news_obj})


def about(request):
    return render(request, 'main/about.html')


def history(request):
    return render(request, 'main/history.html')


def kindergarten(request):
    return render(request, 'main/kindergarten.html')


def school(request):
    return render(request, 'main/school.html')


def lyceum(request):
    return render(request, 'main/lyceum.html')


def religion(request):
    return render(request, 'main/religion.html')


def restaurant(request):
    return render(request, 'main/restaurant.html')


def news(request):
    return render(request, 'main/news.html')


def contacts(request):
    return render(request, 'main/contacts.html')
