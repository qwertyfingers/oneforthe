# Create your views here.
from django.shortcuts import render

def display_image(request):
    return render(request, 'money/display_image.html',)
