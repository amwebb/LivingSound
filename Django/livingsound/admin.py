from django.contrib import admin
from .models import GardenEntry

class GardenAdmin(admin.ModelAdmin):
    readonly_fields = ['username']
    fieldsets = [
        (None, { 'fields': [('picture', 'sound', 'rating', 'message')] } ),
    ]

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        GardenEntry.username = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        obj.save()

# Register your models here.
admin.site.register(GardenEntry, GardenAdmin)

#admin login: username: admin pass: FakePass
#p1 login username: p1 pass: Fake1Pass
#p2 Fake2Pass
