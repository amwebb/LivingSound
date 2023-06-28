from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# create default entries
class GardenEntry(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields

    # pip install pillow
    # Pictures and sound are being uploaded to media folder
    #assign username and date as name
    picture = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Upload an update picture of your plant')

    #Have max length (30 secs?)
    sound = models.FileField(upload_to='sounds/', null=True, blank=True, help_text='Upload a sound file')

    #radial value or buttons
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], 
                                 help_text='Enter the rating of the quality of your plant (out of 5).' + 
                                 '\n| 1 - very poor (not doing well) | \n2 - poor | \n3 - no change | \n4 - good | \n5 - very good (doing very well)')

    message = models.CharField(max_length=300, help_text='Enter the message')

    #timestamp is used to find the newest entry
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.). 
        Name of each entry is username and date."""
        return f'{self.username} ({self.timestamp})'
    
    def ratingPic(self):
        """Returns the picture that corresponds with the rating integer"""
        if self.rating == 1:
            return 'src=static/images/1Out5.png alt=One'
        elif self.rating == 2:
            return 'src=static/images/2Out5.png alt=Two'
        elif self.rating == 3:
            return 'src=static/images/3Out5.png alt=Three'
        elif self.rating == 4:
            return 'src=static/images/4Out5.png alt=Four'
        elif self.rating == 5:
            return 'src=static/images/5Out5.png alt=Five'
        else:
            return 'src=static/images/0Out5.png alt=Zero'
