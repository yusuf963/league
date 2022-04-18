from django.shortcuts import render
from django.http import HttpResponse


def rank(req):
    return HttpResponse('hello from ranks')
