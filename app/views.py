from django.http import HttpResponse

import requests


def index(request):
    return HttpResponse("[app/index]")


def echo(request, q):
    return HttpResponse(f"[app/echo]: {q}")


def search(request, q):
    r = requests.get(f"https://www.google.com/search?&q={q}")
    return HttpResponse(f"[app/request]: {r.text}")