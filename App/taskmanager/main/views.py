from django.shortcuts import render
from .models import ContactUs


def index(request):
    contacts = ContactUs.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Main page',
                                               'contacts': contacts})


def about(request):
    return render(request, 'main/about.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def support(request):
    return render(request, 'main/support.html')

