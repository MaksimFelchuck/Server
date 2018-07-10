
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
from django.views.generic.base import View

def Index(request):
    return render(request, 'home.html')
def Main(request):
    return render(request, 'Main.html')

def Script(request):
        form = ScriptForm(request.POST or  None)
        dict = {'form': form}
        if request.method == 'POST' and form.is_valid():
            data = form.cleaned_data
            new_form = form.save()
            print(data['script'])



        return render(request, 'form.html', dict)



