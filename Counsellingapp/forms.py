from dataclasses import field
from django.contrib.auth.models import User
from django import forms
from .models import User,Doctor,Patient


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields =['']
