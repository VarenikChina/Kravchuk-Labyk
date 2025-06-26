from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Main page view

def main_page(request):
    return HttpResponse('<h1>Main Page</h1><ul>\n<li><a href="/view1/">View 1</a></li>\n<li><a href="/view2/">View 2</a></li>\n<li><a href="/view3/">View 3</a></li>\n<li><a href="/view4/">View 4</a></li>\n<li><a href="/view5/">View 5</a></li>\n</ul>')

# Additional views

def view1(request):
    return HttpResponse('<h1>View 1</h1><a href="/">Back to Main Page</a>')


def view2(request):
    return HttpResponse('<h1>View 2</h1><a href="/">Back to Main Page</a>')


def view3(request):
    return HttpResponse('<h1>View 3</h1><a href="/">Back to Main Page</a>')


def view4(request):
    return HttpResponse('<h1>View 4</h1><a href="/">Back to Main Page</a>')


def view5(request):
    return HttpResponse('<h1>View 5</h1><a href="/">Back to Main Page</a>')
