from django.shortcuts import render
from .models import ContactUs


def index(request):
    contacts = ContactUs.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Main page',
                                               'contacts': contacts})


def about(request):
    return render(request, 'main/about.html')


def history(request):
    return render(request, 'main/history.html')


def kindergarten(request):
    return render(request, 'main/kindergarten.html')


def school(request):
    return render(request, 'main/school.html')


def college(request):
    return render(request, 'main/college.html')


def religion(request):
    return render(request, 'main/religion.html')


def restaurant(request):
    return render(request, 'main/restaurant.html')


def contacts(request):
    return render(request, 'main/contacts.html')
