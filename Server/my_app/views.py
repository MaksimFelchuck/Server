

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    records = script.objects.all()

    context = {
        'dict': records
    }
    return render(request, 'home.html',context)



def Script(request):
        form = ScriptForm(request.POST or  None)
        dict = {'form': form}
        if request.method == 'POST' and form.is_valid():
            data = form.cleaned_data
            new_form = form.save()
            print(data['script'])



        return render(request, 'form.html', dict)



