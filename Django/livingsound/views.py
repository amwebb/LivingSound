from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect


from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from .models import GardenEntry
from .forms import GardenForm
# Decorator for Login Required
from django.contrib.auth.decorators import login_required
from natsort import natsort_keygen
from plotly.offline import plot
from plotly.graph_objs import Scatter

natsort_key = natsort_keygen()

@login_required(login_url='/accounts/login/')
def garden(request):
    entries = []
    non_admin_users = User.objects.filter(groups__name='Participants') #.order_by('username')

    for user in non_admin_users:
        try:
            entry = GardenEntry.objects.filter(username=user).latest('timestamp')
            entries.append(entry)
        except ObjectDoesNotExist:
            pass
        
    entries.sort(key=lambda entry: natsort_key(str(entry.username)))

    context = {
        "data" : entries,
    }

    return render(request, 'livingsound/garden.html', context=context)

@login_required(login_url='/accounts/login/')
def submission(request):
    """This saves the garden form and collects the username"""
    if request.method == "POST":
        form = GardenForm(request.POST, request.FILES)
        if form.is_valid():
            GardenEntry = form.save(commit=False)
            GardenEntry.username = request.user
            GardenEntry.save()
            
            #This is supposed to redirect to avoid double submission but hasn't worked yet
            return redirect("success")
        else: 
            print("This form is not valid")
    form = GardenForm()
    return render(request, 'livingsound/submission.html', {"form": form, 
                                                           "user": request.user.username,})


def success(request):
    return render(request, 'livingsound/success.html')

#individual pages

@login_required(login_url='/accounts/login/')
def profile(request, username):
    """Returns QuerySet of all entries of specified user and creates a graph that shows the ratings over time."""
    u = User.objects.get(username=username)
    try:
        profileEnts = GardenEntry.objects.filter(username=u.id)
    except ObjectDoesNotExist:
        pass

    ratingLst = []
    for ent in profileEnts:
        ratingLst.append(ent.rating)
    
    x_data = []
    for x in range(len(ratingLst)):
        x_data.append(x)

    plot_div = plot([Scatter(x=x_data, y=ratingLst, mode='lines', 
                             name='p1 Rating Chart', opacity=0.8, marker_color='green')],
                             output_type='div', include_plotlyjs=False, config={'responsive': True})

    return render(request, 'livingsound/profile.html',  {"profileEnts": profileEnts,
                                                         "username": u.username,
                                                         "plot_div": plot_div})

