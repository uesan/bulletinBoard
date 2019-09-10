from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'bulletinBoard/index.html')


from django.shortcuts import render

# Create your views here.
