from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
def insert_topic(request):
    tn=input('enter the topic:')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic insert successfully')
def insert_webpage(request):
    tn=input('enter the topic:')
    n=input('enter the name:')
    u=input('enter the urls:')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
    W.save()
    return HttpResponse('webpage updated successfully')
def accrec(request):
    tn=input('enter the topic:')
    n=input('enter the name:')
    u=input('enter the urls:')
    a=input('enter the author name:')
    d=input('enter the date:')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    wob2=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
    wob2.save()
    aob1=AccessRecord.objects.get_or_create(name=wob2,author=a,date=d)[0]
    aob1.save()
    return HttpResponse('webpage updated successfully')



