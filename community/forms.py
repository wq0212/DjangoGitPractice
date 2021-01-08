from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = MainBoard
        fields = ['title','contents']