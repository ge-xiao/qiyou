from django.shortcuts import render
from django.http import HttpResponse
from qiyou.models import user
import json

def index(request):

    print(request.method)
    print(request.body)
    print(user.objects.get(name="ge"))
    
    return HttpResponse("ajjja")

    