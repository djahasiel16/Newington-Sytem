from django import forms
from .models import DavaoAuthorizedPersons, CotabatoAuthorizedPersons, NegrosAuthorizedPersons, SurigaoAuthorizedPersons
from davao_requests.models import AuthorizedPersons as dvo_authorizedPerson
from cotabato_requests.models import AuthorizedPersons as cbt_authorizedPerson
from negros_requests.models import AuthorizedPersons as ngro_authorizedPerson
from surigao_requests.models import AuthorizedPersons as srgo_authorizedPerson

class DavaoAuthorizedPersonsForm(forms.ModelForm):
    class Meta:
        model = DavaoAuthorizedPersons
        fields = [
            'firstname',
            'middle_initial',
            'lastname',
            'role'
        ]