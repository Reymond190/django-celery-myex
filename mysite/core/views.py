
from django.shortcuts import render, HttpResponse
from .tasks import mitasc




def myview(request):
    mitasc.delay()
    return HttpResponse('hello')            #start task on this on localhost:8000/ray