from django import template

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