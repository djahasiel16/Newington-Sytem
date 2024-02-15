from django import forms
from .models import NegrosRequestHeader, NegrosRequestItems, AuthorizedPersons, Monitoring, Persons

class NegrosRequestHeaderForm(forms.ModelForm):
    class Meta:
        model = NegrosRequestHeader
        fields = [
            'rs_number',
            'payee',
            'particulars',
            'project',
            'urgent',
            'date_requested',
            'date_needed'
        ]

    rs_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    particulars = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    payee = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','max_length':'"100"'}))
    date_requested = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date', 'autocomplete':'off'}))
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date', 'autocomplete':'off'}))


class NegrosRequestItemsForm(forms.ModelForm):
    class Meta:
        model = NegrosRequestItems
        fields = [
            'header',
            'item_id',
            'ignore',
            'description',
            'quantity',
            'unit',
            'unit_cost',
            'amount',
            'served',
        ]

        labels = {
            'header':'RS NO.',
            'item_id':'PROJECT ID',
            'description':'DESCRIPTION',
            'quantity':'QUANTITY',
            'unit':'UNIT',
            'unit_cost':'UNIT COST',
            'amount':'AMOUNT',
            'served':'SERVED'         
        }

        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'item_id':forms.TextInput(attrs={'class':'form-control'}),
            'ignore':forms.CheckboxInput(attrs={'class':'from-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control quantity', 'id':'qty'}),
            'unit':forms.TextInput(attrs={'class':'form-control amnt'}),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control unit_cost', 'id':'unit_cost'}),
            'amount':forms.NumberInput(attrs={'class':'form-control amount amnt', 'id':'amount'}),
        }
        
        
class NegrosRequestAddItemsForm(forms.ModelForm):
    class Meta:
        model = NegrosRequestItems
        fields = [
            'header',
            'item_id',
            'ignore',
            'description',
            'quantity',
            'unit',
            'unit_cost',
            'amount',
            'served',
        ]

        labels = {
            'header':'RS NO.',
            'item_id':'PROJECT ID',
            'description':'DESCRIPTION',
            'quantity':'QUANTITY',
            'unit':'UNIT',
            'unit_cost':'UNIT COST',
            'amount':'AMOUNT',
            'served':'SERVED'         
        }

        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'item_id':forms.TextInput(attrs={'class':'form-control'}),
            'ignore':forms.CheckboxInput(attrs={'class':'from-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control quantity', 'id':'qty'}),
            'unit':forms.TextInput(attrs={'class':'form-control amnt'}),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control unit_cost', 'id':'unit_cost'}),
            'amount':forms.NumberInput(attrs={'class':'form-control amount amnt', 'id':'amount'}),
        }

class PersonsChoicesField(forms.ModelChoiceField):
    def labels_from_instance(self, obj):
        return obj.name

class AuthorizedPersonsForm(forms.ModelForm):
    TITLE_CHOICES = {
        'RB':'Requested by',
        'PB':'Prepared by',
        'CB':'Checked by',
        'RA':'Recommending Approval',
        'AB':'Approved by'
    }
    class Meta:
        model = AuthorizedPersons
        fields = [
            'header',
            'name',
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
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Select(attrs={'class':'form-control'}, choices=TITLE_CHOICES),
            'signature':forms.FileInput(attrs={'class':'form-control'})
        }


class MonitoringForm(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = [
            'header',
            'PO_no',
            'PO_date',
            'delivery_date',
            'receiving_report',
            'DR_no',
            'SI_no',
            'OR_no',
            'CR_no',
            'withdrawal_no',
            'item_date'
        ]

        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'PO_no':forms.TextInput(attrs={'class':'form-control'}),
            'PO_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'delivery_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'receiving_report':forms.TextInput(attrs={'class':'form-control'}),
            'DR_no':forms.TextInput(attrs={'class':'form-control'}),
            'SI_no':forms.TextInput(attrs={'class':'form-control'}),
            'OR_no':forms.TextInput(attrs={'class':'form-control'}),
            'CR_no':forms.TextInput(attrs={'class':'form-control'}),
            'withdrawal_no':forms.TextInput(attrs={'class':'form-control'}),
            'item_date':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }

        labels = {
            'header':'Item No.',
            'PO_no':'P.O. No.',
            'PO_date':'P.O. Date',
            'delivery_date':'Delivery Date',
            'receiving_report':'Receiving Report',
            'DR_no':'D.R. No.',
            'SI_no':'S.I. No.',
            'OR_no':'O.R. No.',
            'CR_no':'C.R. No.',
            'withdrawal_no':'Withdrawal No.',
            'item_date':'Date'
        }