
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import *
from .models import script


# Create your views here.
from django.views.generic.base import View


def Main(request):
    records = script.objects.all()

    context = {
        'dict': records
    }
    return render(request, 'Main.html',context)

def Index(request):

    return render(request, 'home.html')



def Script(request):

    if request.method == 'POST':
        index = script()
        index.save()

        return render(request, 'form.html')

def scriptid(request, script_id):

    index = script.objects.get(script_name = script_id)
    text = index.script


    context = {
        'index': index,
        'text': text
    }
    return render(request, 'script_id.html',context)

def Delete_script(request, script_id):

    try:
        if request.method == 'POST':
            index = script(script_id)

            index.delete()

            return redirect(Reverse('home'))
    except():
        return render(request, 'home.html')
