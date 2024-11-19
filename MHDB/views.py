from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def main_view(request):
    return render(request, 'index.html')