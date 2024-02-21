from django import template
from main.forms import PersonnelForm

register = template.Library()

@register.filter(name='clean_int')
def clean_int(value):
    try:
        if int(value) == 0:
            return ""
        else:
            return value
    except ValueError:
        if value == '0.00':
            return ""
        else:
            return value

@register.filter(name='clean_empty')
def clean_empty(value):
    if value == '' or not value:
        return "--"
    else:
        return value
    
@register.inclusion_tag('main/actions/modals/modal_form.html')
def personnelFormModal():
    form = PersonnelForm()
    return {'form':form}

@register.filter(name="clean_decimal")
def clean_decimal(value):
    try:
        if value > int(value):
            return value
        else:
            return int(value)
    except ValueError:
        return ""