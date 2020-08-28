from django import forms
from .models import Traits

class TraitsForm(forms.ModelForm):

    class Meta:
        model = Traits
        fields = ('title', 'text')

