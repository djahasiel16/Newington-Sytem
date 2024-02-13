from django import template
from cotabato_requests.forms import AuthorizedPersonsForm

register = template.Library()

@register.inclusion_tag('main/actions/globalAddPerson.html')
def cbt_renderPersonForm(rs_number):
    form = AuthorizedPersonsForm()
    return {'form':form}
