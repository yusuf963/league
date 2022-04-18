from django.shortcuts import render
from django.http import HttpResponse


def club(req):
    return HttpResponse('clubs route')
