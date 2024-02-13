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
        return value
