"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from my_app import views



from my_app.views import *
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('script/', Script, name='script'),
    path('home/', Main, name='home'),
    path('home/<str:script_id>/delete', Delete_script, name='Delete_script'),
    path('home/edit/<str:script_id>', Edit, name='edit'),



]
