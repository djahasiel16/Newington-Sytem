from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.http.response import HttpResponse
from .models import CotabatoRequestHeader, CotabatoRequestItems, AuthorizedPersons
from .forms import CotabatoRequestHeaderForm, CotabatoRequestItemsForm, AuthorizedPersonsForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# timezone.now().year

# Create your views here.
def dashboard(request):
    return render(request, 'main/actions/dashboard.html', {'title':'Cotabato'})


def add_request_view(request):
    if request.method == 'POST':
        form = CotabatoRequestHeaderForm(request.POST, instance=CotabatoRequestHeader(user=User.objects.get(pk=request.user.id)))
        if form.is_valid:
            rs_number = request.POST['rs_number']
            form.save()
            messages.success(request, "Request Added Successfully")
            # return redirect(reverse('cotabato_add_items', kwargs={'rs_number':rs_number}))
            return redirect(reverse('cotabato_add_authorizedPerson', kwargs={'rs_number':rs_number}))
        
    rs_number = f"CBT{timezone.now().year}-"
    try:
        idx = CotabatoRequestHeader.objects.all()
        rs_number += str(len(idx)+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = CotabatoRequestHeaderForm(initial={'rs_number':rs_number})
    return render(request, 'main/actions/add_request.html', {'form':form, 'title':'Cotabato'})

def add_items_view(request, rs_number):
    init_data = {'header':rs_number}
    items = CotabatoRequestItems.objects.filter(header=CotabatoRequestHeader.objects.get(pk=rs_number))
    if request.method == "POST":
        form = CotabatoRequestItemsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Item Added Successfully")
        
    form = CotabatoRequestItemsForm(initial=init_data)
    return render(request, 'main/actions/add_items.html', {'form':form, 'items':items, 'title':'Cotabato'})

def rs_view(request, rs_number):
    header = CotabatoRequestHeader.objects.get(pk=rs_number)
    items = CotabatoRequestItems.objects.filter(header=header)
    total = items.aggregate(amount_sum=Sum('amount'))['amount_sum']
    persons = AuthorizedPersons.objects.filter(header=CotabatoRequestHeader.objects.get(pk=rs_number))
    person_details = {}
    for person in persons:
        name = ' '.join([person.firstname, "" if str(person.middle_initial) == 'None' else person.middle_initial+'.', person.lastname])
        person_details[person.title.replace(" ","_")] = (name, person.signature)
        print(person_details)

    return render(request, 'main/actions/rsSlip.html', {'header':header, 'items':items, 'fields':list(range(1,16-len(items)+1)), 'total':total, 'persons':person_details, 'title':'Cotabato'})
        
def add_authorizedPerson_view(request, rs_number):
    init_data = {'header':CotabatoRequestHeader.objects.get(pk=rs_number)}
    if request.method == 'POST':
        form = AuthorizedPersonsForm(request.POST, request.FILES, initial=init_data)
        if form.is_valid:
            form.save()
            messages.success(request, "Person Added Successfully")
            return redirect(reverse('cotabato_add_authorizedPerson', kwargs={'rs_number':rs_number}))
        
    form = AuthorizedPersonsForm(initial=init_data)
    return render(request, 'main/actions/add_authorizedPerson.html', {'form':form, 'title':'Cotabato'})


def list_view_requests(request):
    rs = CotabatoRequestHeader.objects.all()
    return render(request, 'main/actions/list_view_request.html', {'rs':rs, 'title':'Cotabato'})


def edit_item_view(request, rs_id):
    # header=CotabatoRequestHeader.objects.get(pk=rs_id)
    item = CotabatoRequestItems.objects.get(pk=rs_id)
    
    form = CotabatoRequestItemsForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Item Updated Successfully")
        return redirect(reverse(list_view_items))
    else:
        return render(request, 'main/actions/edit_item.html', {'form':form, 'title':'Cotabato'})

def edit_request_view(request, rs_number):
    rs = CotabatoRequestHeader.objects.get(pk=rs_number)
    form = CotabatoRequestHeaderForm(request.POST or None, instance=rs)

    if form.is_valid():
        form.save()
        messages.success(request, "Request Updated Successfully")
        return redirect(reverse(list_view_requests))
    else:
        return render(request, 'main/actions/edit_request.html', {'form':form, 'title':'Cotabato'}) 
 
def edit_authorizedPerson_view(request, rs_number):
    instance_data = AuthorizedPersons(CotabatoRequestHeader.objects.get(pk=rs_number))
    if request.method == 'POST':
        form = AuthorizedPersonsForm(
            request.POST,
            request.FILES,
            instance=instance_data
            )
        
        if form.is_valid():
            form.save()
            return redirect(reverse('Cotabato'))
        
    form = AuthorizedPersonsForm(instance=instance_data)
    return render(request, 'main/actions/add_authorizedPerson.html', {'form':form, 'title':'Cotabato'})


def list_view_items(request):
    items = CotabatoRequestItems.objects.all()
    return render(request, 'main/actions/list_view_items.html', {'items':items, 'title':'Cotabato'})


def go_back(request):
    referer = request.META.get('HTTP_REFERER')

    return redirect(referer)

def delete_item(request, item_id):
    item = CotabatoRequestItems.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Deleted Successfully")
    return redirect(reverse(list_view_items))