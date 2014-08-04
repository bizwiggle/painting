#for testing only
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    context = {
        'page_title':'Painting Index Title',
        'page_description':'Enter page description',
    }
    return render(request, 'index.html', context)

def our_process(request):
    return HttpResponse("Painting Our Process")

def services(request):
    context = {
        'page_title':'Painting About Title',
        'page_description':'Enter page description',
    }
    return render(request, 'services.html', context)

def residential(request):
    return HttpResponse("Painting Residential Service")

def comercial(request):
    return HttpResponse("Painting Comercial Service")

def other(request):
    return HttpResponse("Painting Other Services")

def portfolio(request):
    context = {
        'page_title':'Painting Portfolio Title',
        'page_description':'Enter page description',
    }
    return render(request, 'portfolio.html', context)

def about(request):
    context = {
        'page_title':'Painting About Title',
        'page_description':'Enter page description',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'page_title':'Painting Contact Title',
        'page_description':'Enter page description',
    }
    return render(request, 'contact.html', context)


