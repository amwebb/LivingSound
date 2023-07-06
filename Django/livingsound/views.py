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
import plotly.graph_objs as go

natsort_key = natsort_keygen()

@login_required(login_url='/accounts/login/')
def garden(request):
    entries = []
    non_admin_users = User.objects.filter(groups__name='Participants') #.order_by('username')

    for user in non_admin_users:
        try:
            entry = GardenEntry.objects.filter(username=user).latest('timestamp')
        except ObjectDoesNotExist:
            entry = GardenEntry()
            entry.username = user   
        entries.append(entry)
        
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

@login_required(login_url='/accounts/login/')
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
    
    userSound = "{0}.mp3".format(u.username)

    if len(profileEnts) > 0:
        reverse = []
        ratingLst = []
        x_data = []
        for ent in profileEnts:
            ratingLst.append(ent.rating)
            reverse.insert(0, ent)
            x_data.append(ent.timestamp)
        
        fig = go.Figure(go.Scatter(x=x_data, y=ratingLst, mode='lines', name='p1 Rating Chart', opacity=0.8, marker_color='green'))
        fig.update_layout(
            yaxis = dict(
                tickmode = 'array',
                tickvals = [1, 2, 3, 4, 5],
                ticktext = ['😩','☹️','😐','🙂','😄'],
                tickfont = dict(size=20),
                title = "Ratings"
                ),
            xaxis = dict(
                tickfont = dict(size=20),
                tickformat = "%b %e",
                title = "Dates"
            )
        )

        plot_div = plot(fig, output_type='div', include_plotlyjs=False, config={'responsive': True})

        return render(request, 'livingsound/profile.html',  {"profileEnts": reverse,
                                                            "username": u.username,
                                                            "userSound": userSound,
                                                            "plot_div": plot_div})
    else:
        return render(request, 'livingsound/profile.html', {"username": u.username})
