from django.shortcuts import render
from django.http import HttpResponse


def dashboard_admin(request):
    return HttpResponse("bienvenue dans l'espace adminstration")



