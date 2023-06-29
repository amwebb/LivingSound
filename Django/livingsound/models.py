from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# create default entries
class GardenEntry(models.Model):
    """A typical class defining a model, derived from the Model class."""

    #Directory for files to go to specific folders
    def user_directory_path_img(instance, filename):
        return "uploads/{0}/images/{1}_{2}".format(instance.username, datetime.now(), filename)
    
    def user_directory_path_sound(instance, filename):
        return "uploads/{0}/sound/{1}_{2}".format(instance.username, datetime.now(), filename)

    # Fields

    # pip install pillow
    # Pictures and sound are being uploaded to media folder
    #assign username and date as name
    #user directory - username/imagesorsound/timestamp+filename
    picture = models.ImageField(upload_to=user_directory_path_img, null=True, blank=True, help_text='Upload an update picture of your plant')

    sound = models.FileField(upload_to=user_directory_path_sound, null=True, blank=True, help_text='Upload a sound file')

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
            return 'static/images/1Out5.png'
        elif self.rating == 2:
            return 'static/images/2Out5.png'
        elif self.rating == 3:
            return 'static/images/3Out5.png'
        elif self.rating == 4:
            return 'static/images/4Out5.png'
        elif self.rating == 5:
            return 'static/images/5Out5.png'
        else:
            return 'static/images/0Out5.png'
