from django.shortcuts import render
from django.http import HttpResponse


def player(req):
    return HttpResponse('hi there from player')
