from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def count(request):
    if request.method == 'GET':
        return redirect('index')