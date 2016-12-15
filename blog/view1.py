from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    resKv = {}
    resKv["res"] = "sweet"
    return render(request, "a.html", resKv)

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
