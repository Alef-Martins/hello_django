from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome):
    return HttpResponse(f'Hello {nome}')