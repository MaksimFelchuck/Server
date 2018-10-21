
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import *
from .models import script


# Create your views here.
from django.views.generic.base import View

import datetime
def Main(request):
    records = script.objects.all()


    context = {
        'dict': records
    }

    return render(request, 'Main.html',context)

def Index(request):

    return render(request, 'home.html')



def Script(request):
    form = ScriptForm(request.POST or None)
    dict = {'form': form,
            'date': str(datetime.datetime.now())[:10]}
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'form.html', dict)


def scriptid(request, script_id):

    index = get_object_or_404(script, script_name = script_id)
    text = index.script
    context = {
        'index': index,
        'text': text
    }
    if request.method == 'POST':
        index.script = request.POST.get('script')
        index.save()
        return redirect(reverse('home'))

    else:
        return render(request, 'script_id.html',context)

def Delete_script(request, script_id):

    if request.method == 'GET':
        index = script.objects.get(script_name= script_id)
        index.delete()
        return redirect(reverse('home'))



def Edit(request, script_id):

    index = script.objects.get(script_name=script_id)
    text = index.script
    context = {
        'index': index,
        'text': text,
        'date': str(datetime.datetime.now())[:10]
            }
    if request.method == 'POST':

        index.script = request.POST.get('script')
        index.save()
        return redirect(reverse('home'))

    return render(request, 'form_edit.html', context)


