from django.shortcuts import render

def bakery_home(request):
    return render(request, "bakery.html")