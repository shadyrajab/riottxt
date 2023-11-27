from django.shortcuts import render

# Create your views here.
def riot(request):
    return render(request, 'auth/riot.txt')