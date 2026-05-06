from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Client, Provider, ServiceCategory, JobRequest, JobAssignment, Payment, Review

def index(request):
    return HttpResponse("Hello, world !!!")

def clientDashboard(request):
    return HttpResponse("Ayoo boss man !!!")

def jobRequest(request):
    return HttpResponse("This the job ???")

def provider(request):
    return HttpResponse("who you sliding with ???")

def payment(request):
    return HttpResponse("Pay Now !!!")

def review(request):
    return HttpResponse("Gang is this right !!!")