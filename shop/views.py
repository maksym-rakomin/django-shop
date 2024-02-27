from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Category

# Create your views here.


def index(request):
    courses = Course.objects.all()
    res = f"<ul>{
        ''.join(['<li>' + str(course) + '</li>' for course in courses])
    }</ul>"
    return HttpResponse(res)
