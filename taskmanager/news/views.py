from django.shortcuts import render
from .models import Articles


def news(request):
    news_obj = Articles.objects.order_by('-date')
    return render(request, 'main/news.html', {'news_obj': news_obj})
