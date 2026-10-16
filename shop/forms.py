from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['owner_name', 'phone_number', 'animal', 'pet_name', 'date', 'comments']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}