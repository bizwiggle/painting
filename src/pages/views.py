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

def why_us(request):
    context = {
        'page_title':'Painting Our Process Title',
        'page_description':'Enter page description',
    }
    return render(request, 'why_us.html', context)

def services(request):
    context = {
        'page_title':'Painting About Title',
        'page_description':'Enter page description',
    }
    return render(request, 'services.html', context)

def residential(request):
    context = {
        'page_title':'Painting Residential Painting Title',
        'page_description':'Enter page description',
    }
    return render(request, 'residential.html', context)

def comercial(request):
    context = {
        'page_title':'Painting Comercial Painting Title',
        'page_description':'Enter page description',
    }
    return render(request, 'comercial.html', context)

def other(request):
    context = {
        'page_title':'Painting Other Services Title',
        'page_description':'Enter page description',
    }
    return render(request, 'other.html', context)

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


