from django.shortcuts import render
from .models import Finch

finch = [
    {'name': 'Evening Grosbeak', 'location': 'Northern and montane forests', 'description': 'The Evening Grosbeak does not have a complex song, but rather draws from a collection of sweet, piercing notes and burry chirps.'},
    {'name': 'Brown-capped Rosy-Finch', 'location': 'Alpine tundra', 'description': 'Brown-capped Rosy-Finches are the most sedentary rosy-finch. Unlike the Black Rosy-Finch, this species will sometimes nest in abandoned buildings.'},
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })