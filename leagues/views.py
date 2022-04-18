from django.shortcuts import render
from django.http import HttpResponse


def league(req):
    return HttpResponse('hi there from leagues')
