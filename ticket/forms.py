from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Ticket, OrderItem, Address


User = get_user_model()


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "depart",
            "destination",
            "date_du_vol",
            "heure_du_vol",
            "places_restantes",
            "prix_ticket",
        ]
        widgets = {
        'date_du_vol': forms.TextInput(attrs={'type': 'date'}),
        'heure_du_vol': forms.TextInput(attrs={'type': 'Time'})

        }




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': _("Your name")
    }), label=_('Name'))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': _("Your e-mail")
    }), label=_('Email'))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': _('Your message')
    }), label=_('Message'))


class AddToCartForm(forms.ModelForm):
    class Meta:
        model =OrderItem
        fields = ['quantity']


class PassengerDetailsForm(forms.Form):

    civilité = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mr or Mme or Mlle'}),
                  max_length=50, required=False)
    prénom = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Prénom'}),
                  max_length=50, required=False)
    nom_de_famille = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nom de famille'}),
                  max_length=50, required=False)

    selected_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id=user_id)

        address_qs = Address.objects.filter(
            user=user,
            address_type='S'
        )
       

        self.fields['selected_address'].queryset = address_qs

    def clean(self):
        data = self.cleaned_data

        selected_address = data.get('selected_address', None)
        if selected_address is None:
            if not data.get('civilité', None):
                self.add_error("civilité",
                               "Please fill in this field")
            if not data.get('prénom', None):
                self.add_error("prénom",
                               "Please fill in this field")
            if not data.get('nom_de_famille', None):
                self.add_error("nom_de_famille", "Please fill in this field")

      