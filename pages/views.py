from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from .models import login
from .forms import login_form

# Create your views here.

def home(request):

    url = "https://jsonplaceholder.typicode.com/posts"

    res = requests.get(url)

    g = res.json()

    return JsonResponse(g, safe=False)

def master(request):

    d = request.GET.get("number", 0)

    try:

        d = int(d)

    except ValueError:

        d = 0

    h = d * 2

    return HttpResponse(f"Double of your number is: {h}")

def apises(request):

    d = request.GET.get("id", 1)

    try:

        d = int(d)

    except ValueError:

        d = 1


    url = f"https://jsonplaceholder.typicode.com/posts/{d}"

    try:

        res = requests.get(url, timeout=5)

    except requests.exceptions.RequestException:

        return JsonResponse({"error" : "External service unavailable"}, status=503)

    if res.status_code !=200:

        return JsonResponse({"error" : "not found"}, status=404)

    g = res.json()

    return JsonResponse(g)

def template(request):

    return render(request, 'pages/template.html', {'name': 'alaa', 'age': 3434665435452350})

def about(request):

    if request.method=="POST":
        form= login_form(request.POST)
        if form.is_valid():
            form.save()

    else:

        form = login_form()

    # name = request.POST.get('username')
    # password= request.POST.get('password')
    # data=login(username=name, password=password)
    # data.save()

    return render(request, 'pages/about.html', {'log': form})
