from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.timezone import datetime
from .models import GardenEntry

def garden(request):
    """Filter each username. find the most recent entry by that username.
    add it to the context list as 'username'Ent. use the values in each
    username to fill in info in entry.html"""

    try:
        # Get the latest entry for the username 'pq'
        entries = GardenEntry.objects.filter(username='p1').latest('timestamp')
    except ObjectDoesNotExist:
        entries = None

    context = {
        'entries': [entries] if entries else [],
    }

    return render(request, 'entry.html', context=context)

def latest_entry(request, username):
    latest_entry = GardenEntry.objects.filter(username=username).latest('timestamp')
    return render(request, 'latest_entry.html', {'entry': latest_entry})
