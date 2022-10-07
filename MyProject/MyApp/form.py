from django .forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta: # Data about data
        model=Person
        fields='__all__'
