from django.shortcuts import render
from .models import Newstable


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
    news = Newstable.objects.order_by('-date')
    return render(request, 'main/news.html', {'news': news})


def contacts(request):
    return render(request, 'main/contacts.html')
