from django import forms
from .models import CotabatoRequestHeader, CotabatoRequestItems

class CotabatoRequestHeaderForm(forms.ModelForm):
    class Meta:
        model = CotabatoRequestHeader
        fields = [
            'rs_number',
            'particulars',
            'payee',
            'project',
            'urgent',
            'date_requested',
            'date_needed'
        ]

    rs_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    particulars = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    payee = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date_requested = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'id':'requested_datepicker'}))
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'id':'needed_datepicker'}))