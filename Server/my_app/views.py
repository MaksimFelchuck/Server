
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


def home(request):
    context = {'context':'Hallo World!!'}

    return render(request, 'home.html', context)



class Index(View):

    def get(self, request):


        return render(request, 'home.html')
    def post(self, request):
        return HttpResponse('POST')


