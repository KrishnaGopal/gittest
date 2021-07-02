from django.http import HttpResponse
from django.shortcuts import redirect
from .. import views
def homepage1(request):
        return redirect(views.homepage) 
