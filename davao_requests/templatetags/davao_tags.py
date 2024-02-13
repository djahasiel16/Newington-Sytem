from django import template
from davao_requests.forms import AuthorizedPersonsForm, DavaoRequestHeaderForm, MonitoringForm, DavaoRequestItemsForm, DavaoRequestAddItemsForm
from davao_requests.models import DavaoRequestHeader, Monitoring, DavaoRequestItems, AuthorizedPersons
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('main/actions/globalAddPerson.html')
def renderPersonForm():
    form = AuthorizedPersonsForm()
    return {'form':form}


@register.inclusion_tag('main/actions/modals/modal_add_requestForm.html')
def renderAddRequestForm():
    rs_number = f"DVO{timezone.now().year}-"
    try:
        idx = DavaoRequestHeader.objects.all()
        rs_number += str(len(idx)+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = DavaoRequestHeaderForm(initial={'rs_number':rs_number})
    return {'form':form, 'title':'Davao'}

@register.filter(name="getid")
def getid(string):
    try:
        id = string[string.index('[')+1:string.index(']')]
        return id
    except:
        return ""

@register.inclusion_tag('main/actions/modals/modal_update_monitoring.html')
def monitoringModalForm(id):
    inst = Monitoring.objects.get(pk=id)
    form = MonitoringForm(instance=inst)
    return {'form':form}


@register.filter(name='clean_empty')
def clean_empty(value):
    if value == '' or not value:
        return "--"
    else:
        return value
    

@register.inclusion_tag('main/actions/modals/modal_edit_request.html')
def editRequestModalForm(rs_number):
    rs = DavaoRequestHeader.objects.get(pk=rs_number)
    form = DavaoRequestHeaderForm(instance=rs)

    return {'form':form, 'title':'Davao'}
    

@register.inclusion_tag('main/actions/modals/modal_form.html')
def addItemsModal(rs_number):
    form = DavaoRequestAddItemsForm(initial={'header':rs_number})
    return {'form':form}

@register.inclusion_tag('main/actions/modals/modal_form.html')
def editItemsModal(item_id):
    form = DavaoRequestAddItemsForm(instance=DavaoRequestItems.objects.get(pk=item_id))
    return {'form':form}

@register.inclusion_tag('main/actions/modals/modal_form.html')
def editItemModal(item_id):
    instance = DavaoRequestItems.objects.get(pk=item_id)
    form = DavaoRequestItemsForm(instance=instance)
    
    return {'form':form}

@register.inclusion_tag('main/actions/modals/modal_form.html')
def editPersonModal(person_id):
    instance = AuthorizedPersons.objects.get(pk=person_id)
    form = AuthorizedPersonsForm(instance=instance)
    
    return {'form':form}