from django.shortcuts import render
from django.http import HttpRequest
from . import views


def club(req):
    return HttpRequest(req, 'clubs route')
