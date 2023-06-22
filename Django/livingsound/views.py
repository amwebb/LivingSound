from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from .models import GardenEntry

def garden(request):
    """Filter each username. find the most recent entry by that username.
    add it to the context list as 'username'Ent. use the values in each
    username to fill in info in entry.html"""

    allEnts = GardenEntry.objects.all()

    #Probably not the most effecient 
    try:
        # Get the latest entry for the username 'pq'
        p1Ent = GardenEntry.objects.filter(username='P1').latest('timestamp')
    except ObjectDoesNotExist:
        p1Ent = None

    try:
        p2Ent = GardenEntry.objects.filter(username='P2').latest('timestamp')
    except ObjectDoesNotExist:
        p2Ent = None

    try:
        p3Ent = GardenEntry.objects.filter(username='P3').latest('timestamp')
    except ObjectDoesNotExist:
        p3Ent = None

    try:
        p4Ent = GardenEntry.objects.filter(username='P4').latest('timestamp')
    except ObjectDoesNotExist:
        p4Ent = None

    try:
        p5Ent = GardenEntry.objects.filter(username='P5').latest('timestamp')
    except ObjectDoesNotExist:
        p5Ent = None

    try:
        p6Ent = GardenEntry.objects.filter(username='P6').latest('timestamp')
    except ObjectDoesNotExist:
        p6Ent = None
    
    try:
        p7Ent = GardenEntry.objects.filter(username='P7').latest('timestamp')
    except ObjectDoesNotExist:
        p7Ent = None

    try:
        p8Ent = GardenEntry.objects.filter(username='P8').latest('timestamp')
    except ObjectDoesNotExist:
        p8Ent = None

    try:
        p9Ent = GardenEntry.objects.filter(username='P9').latest('timestamp')
    except ObjectDoesNotExist:
        p9Ent = None

    try:
        p10Ent = GardenEntry.objects.filter(username='P10').latest('timestamp')
    except ObjectDoesNotExist:
        p10Ent = None

    try:
        p11Ent = GardenEntry.objects.filter(username='P11').latest('timestamp')
    except ObjectDoesNotExist:
        p11Ent = None

    try:
        p12Ent = GardenEntry.objects.filter(username='P12').latest('timestamp')
    except ObjectDoesNotExist:
        p12Ent = None

    context = {
        'p1Ent': p1Ent,
        'p2Ent': p2Ent,
        'p3Ent': p3Ent,
        'p4Ent': p4Ent,
        'p5Ent': p5Ent,
        'p6Ent': p6Ent,
        'p7Ent': p7Ent,
        'p8Ent': p8Ent,
        'p9Ent': p9Ent,
        'p10Ent': p10Ent,
        'p11Ent': p11Ent,
        'p12Ent': p12Ent,

    }

    return render(request, 'entry.html', context=context)

def latest_entry(request, username):
    latest_entry = GardenEntry.objects.all().filter(username=username).latest('timestamp')
    return render(request, 'latest_entry.html', {'entry': latest_entry})


