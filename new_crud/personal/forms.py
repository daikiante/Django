from django import forms
from .models import ALLInfo

class ALLInfoForm(forms.ModelForm):
    class Meta:
        model = ALLInfo
        fields = [
            'name',
            'work',
            'experience',
            'total_salary',
            'email'
        ]