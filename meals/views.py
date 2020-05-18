from django.shortcuts import render

def index(request):
    """The home page for meal planner"""
    return render(request, 'meals/index.html')  