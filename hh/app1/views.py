# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import Messages,List
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    form=Messages()
    respond='Send Message'
    return render(request, 'donate.html',{'form':form,'respond':respond})

def message_sent(request):
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            respond='Your Message has been sent successfully!'
            return render(request,'donate.html',{'data':data,'respond':respond,})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'donate.html',{'data':data,'respond':respond,})

def contact(request):
    form=Messages()
    respond='Send Message'
    return render(request, 'contact.html',{'form':form,'respond':respond})

def message_sent2(request):
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            respond='Your Message has been sent successfully!'
            return render(request,'donate.html',{'data':data,'respond':respond,})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'donate.html',{'data':data,'respond':respond,})


def report(request):
    form=List()
    respond='Send Details'
    return render(request, 'Report.html',{'form':form,'respond':respond})


def details_sent(request):
    if request.method=="POST":
        data=List(request.POST)
        if data.is_valid():
            data.save()
            respond='Your Reported Person Will Be Contacted Shortly!'
            return render(request,'Report.html',{'data':data,'respond':respond,})
        else:
            data=Messages()
            respond='Your Reported Person Will Be Contacted Shortly!'
            return render(request,'Report.html',{'data':data,'respond':respond,})
