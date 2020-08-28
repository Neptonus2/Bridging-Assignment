from django.shortcuts import render
from .models import Traits

def cv(request):
    return render(request, 'cv.html', {})