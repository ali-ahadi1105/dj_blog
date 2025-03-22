from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello from django blog")


def api(request):
    data ={
        "1": {
            "title": "First article1",
            "description": "First article in dj blog",
            "id": 21
        },
        "2": {
            "title": "Second article1",
            "description": "Second article in dj blog",
            "id": 22
        },
        "3": {
            "title": "Third article1",
            "description": "Third article in dj blog",
            "id": 23
        }
    }
    return JsonResponse(data)