from django.shortcuts import render
from django.http import HttpResponse


def match(req):
    return HttpResponse('hello from matches')
