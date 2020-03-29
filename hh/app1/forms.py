from django import forms
from .models import Responses,ReportedPoor
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ('message', 'name','email', 'contact' )

class List(forms.ModelForm):
    class Meta:
        model = ReportedPoor
        fields = ('name', 'contact','address', 'cnic' )