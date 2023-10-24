from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse


def welcome(request):
    return render(request, 'index.html')