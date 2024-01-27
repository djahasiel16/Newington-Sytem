from django import forms
from .models import SurigaoRequestHeader, SurigaoRequestItems, AuthorizedPersons

class SurigaoRequestHeaderForm(forms.ModelForm):
    class Meta:
        model = SurigaoRequestHeader
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


class SurigaoRequestItemsForm(forms.ModelForm):
    class Meta:
        model = SurigaoRequestItems
        fields = [
            'header',
            'description',
            'quantity',
            'unit',
            'unit_cost',
            'amount',
            'served',
        ]

        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control', 'id':'qty'}),
            'unit':forms.TextInput(attrs={'class':'form-control amnt'}),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control', 'id':'unit_cost'}),
            'amount':forms.NumberInput(attrs={'class':'form-control amnt', 'id':'amount'}),
        }

class AuthorizedPersonsForm(forms.ModelForm):
    class Meta:
        model = AuthorizedPersons
        fields = [
            'header',
            'firstname',
            'middle_initial',
            'lastname',
            'title',
            'signature'
        ]

        TITLE_CHOICES = {
        'Requested by':'Requested by',
        'Prepared by':'Prepared by',
        'Checked by':'Checked by',
        'Recommending Approval':'Recommending Approval',
        'Approved by':'Approved by'
    }
        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'middle_initial':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Select(attrs={'class':'form-control'}, choices=TITLE_CHOICES),
            'signature':forms.FileInput(attrs={'class':'form-control'})
        }