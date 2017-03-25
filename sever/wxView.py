from django.http import HttpResponse
import hashlib
from django.shortcuts import render

from sever.models import Article


def validate(request):
    signature = request.GET.get("signature", "")
    timestamp = request.GET.get("timestamp", "")
    nonce = request.GET.get("nonce", "")
    echostr = request.GET.get("echostr", "")

    a = hashlib.sha1((signature + timestamp + nonce).encode("utf-8")).hexdigest()

    print("a:\t"+a)
    print("echostr: "+echostr)
    if a == echostr:
        return HttpResponse(a)
    else:
        return HttpResponse("{echostr:%s,res_echostr:%s}" % (echostr, a))


def theJson(request):
    return HttpResponse('{"meta":{"num":1,"total":24},"data":[9,34,12,43,123,41,231,12]}')
