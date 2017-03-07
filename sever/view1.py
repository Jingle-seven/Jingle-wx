from django.http import HttpResponse
from django.shortcuts import render

from sever.models import Article


def hello(request):
    res = []
    res.append({"name":"Tom","age":18})
    res.append("walking")
    res.append("and dying")
    postList = Article.objects.all()
    return render(request, "home.html", {"resList": postList})

def theJson(request):
    return HttpResponse('{"meta":{"num":1,"total":24},"data":[9,34,12,43,123,41,231,12]}')

def theAdd(request):
    a = request.GET['a']
    b = request.GET.get("b",0)
    c = int(a)+int(b)
    return HttpResponse("%s plus %s is %d"%(a,b,c))


def theAdd2(request, a):
    b = request.GET.get("b",0)
    c = int(a) + int(b)
    return HttpResponse("%s plus %s is %d"%(a,b,c))
