from django.shortcuts import render

# Create your views here.

# Render the home page
def index(request) :
    return render(request, 'home/index.html')
