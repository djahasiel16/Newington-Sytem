from django import forms
from .models import DavaoAuthorizedPersons, CotabatoAuthorizedPersons, NegrosAuthorizedPersons, SurigaoAuthorizedPersons
from davao_requests.models import AuthorizedPersons as dvo_authorizedPerson
from cotabato_requests.models import AuthorizedPersons as cbt_authorizedPerson
from negros_requests.models import AuthorizedPersons as ngro_authorizedPerson
from surigao_requests.models import AuthorizedPersons as srgo_authorizedPerson

from .models import Personnel

class DavaoAuthorizedPersonsForm(forms.ModelForm):
    class Meta:
        model = DavaoAuthorizedPersons
        fields = [
            'firstname',
            'middle_initial',
            'lastname',
            'role'
        ]
        
class PersonnelForm(forms.ModelForm):
    TITLE_CHOICES = {
        'RB':'Requested by',
        'PB':'Prepared by',
        'CB':'Checked by',
        'RA':'Recommending Approval',
        'AB':'Approved by'
    }
    class Meta:
        model = Personnel
        fields = [
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
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Select(attrs={'class':'form-control'}, choices=TITLE_CHOICES),
            'signature':forms.FileInput(attrs={'class':'form-control'})
        }

