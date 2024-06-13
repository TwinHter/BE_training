from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Fields is list attributes of model that need to be set up
        fields = '__all__' # fields = ['name', 'body', ....]
        

