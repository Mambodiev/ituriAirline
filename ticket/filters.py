from .models import Ticket
import django_filters
from django_filters.widgets import RangeWidget
from django.forms.widgets import TextInput
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class TicketFilter(django_filters.FilterSet):


    date_du_vol =  django_filters.DateFilter(label="", widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Ticket
        fields = {
            'date_du_vol',
        }
        

    