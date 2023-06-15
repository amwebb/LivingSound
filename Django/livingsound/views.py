from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.timezone import datetime
from .models import GardenEntry

def garden(request):
    """Filter each username. find the most recent entry by that username. 
    (model.objects.all().orberby(-datetime) and pick the newest one)
    add it to the context list as 'username'Ent. use the values in each 
    username to fill in info in entry.html"""

    entries = GardenEntry.objects.all()
    
    now = datetime.now()
    formatted_now = now.strftime("%y, %m, %d")

    p1Ents = GardenEntry.objects.filter(username='P1').values()

    #p1EntDate = p1Ents.order_by(formatted_now)


    context = {
        'entries': entries,
        'p1Ents': p1Ents,
    }

    return render(request, 'entry.html', context=context)


