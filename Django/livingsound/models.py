from django.db import models
from django.urls import reverse


# Will be edited to include all fields once decided
class GardenEntry(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    username = models.CharField(max_length=20, help_text='Enter username')

    # Probably not needed
    UserEntryNum = models.CharField(max_length=20,
                                    help_text='Enter username and entry number (ex. P1Ent1 for user P1 first entry)')

    # How are we storing pictures and sound?
    # pip install pillow
    # upload pictures and sounds to a media folder
    picture = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Upload an update picture of your plant')

    sound = models.FileField(upload_to='sounds/', null=True, blank=True, help_text='Upload a sound file')

    rating = models.IntegerField(help_text='Enter the rating (out of 5)')

    message = models.TextField(max_length=300, help_text='Enter the message')

    # Needs to capture the datetime of the entry
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.UserEntryNum

# Query set for all entries
# All_Entries = GardenEntry.objects.all()
