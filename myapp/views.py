from django.shortcuts import render
from .models import Character
from django.http import HttpResponse

def character_list(request):
    characters = Character.objects.all()
    return render(request, '../templates/character_list.html', {'characters': characters})

def characters_age_50(request):
    characters = Character.objects.filter(age=50)
    return render(request, '../templates/characters_age_50.html', {'characters': characters})