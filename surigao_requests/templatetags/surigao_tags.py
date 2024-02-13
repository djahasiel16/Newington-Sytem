from django import template
from surigao_requests.forms import AuthorizedPersonsForm

register = template.Library()

@register.inclusion_tag('main/actions/globalAddPerson.html')
def renderPersonForm():
    form = AuthorizedPersonsForm()
    return {'form':form}