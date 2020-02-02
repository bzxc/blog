from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from .models import Artical
# Create your views here.

def hello(request):
    article = Artical.objects.get(title='测试文章')
    Title = article.title
    Body = article.body
    return JsonResponse({'title': Title, 'body': Body})
    #return HttpResponse("欢迎访问我的博客首页！")

def blogPage(request):
    return render_to_response("index.html")

def articalPage(request):
    return render_to_response("artical.html")