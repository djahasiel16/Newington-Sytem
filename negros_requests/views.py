from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.http.response import HttpResponse
from .models import NegrosRequestHeader, NegrosRequestItems, AuthorizedPersons
from .forms import NegrosRequestHeaderForm, NegrosRequestItemsForm, AuthorizedPersonsForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# timezone.now().year

# Create your views here.
def dashboard(request):
    return render(request, 'main/actions/dashboard.html', {'title':'Negros'})


def add_request_view(request):
    if request.method == 'POST':
        form = NegrosRequestHeaderForm(request.POST, instance=NegrosRequestHeader(user=User.objects.get(pk=request.user.id)))
        if form.is_valid:
            rs_number = request.POST['rs_number']
            form.save()
            messages.success(request, "Request Added Successfully")
            return redirect(reverse('negros_add_items', kwargs={'rs_number':rs_number}))
        
    rs_number = f"NGRO{timezone.now().year}-"
    try:
        idx = NegrosRequestHeader.objects.all()
        rs_number += str(len(idx)+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = NegrosRequestHeaderForm(initial={'rs_number':rs_number})
    return render(request, 'main/actions/add_request.html', {'form':form, 'title':'Negros'})

def add_items_view(request, rs_number):
    init_data = {'header':rs_number}
    items = NegrosRequestItems.objects.filter(header=NegrosRequestHeader.objects.get(pk=rs_number))
    # items[0].
    if request.method == "POST":
        form = NegrosRequestItemsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Item Addedd Successfully")
        
    form = NegrosRequestItemsForm(initial=init_data)
    return render(request, 'main/actions/add_items.html', {'form':form, 'items':items, 'title':'Negros'})

def rs_view(request, rs_number):
    header = NegrosRequestHeader.objects.get(pk=rs_number)
    items = NegrosRequestItems.objects.filter(header=header)
    total = items.aggregate(amount_sum=Sum('amount'))['amount_sum']
    persons = AuthorizedPersons.objects.filter(header=NegrosRequestHeader.objects.get(pk=rs_number))
    person_details = {}
    for person in persons:
        name = ' '.join([person.firstname, "" if str(person.middle_initial) == 'None' else person.middle_initial+'.', person.lastname])
        person_details[person.title.replace(" ","_")] = (name, person.signature)
        print(person_details)

    return render(request, 'main/actions/rsSlip.html', {'header':header, 'items':items, 'fields':list(range(1,16-len(items)+1)), 'total':total, 'persons':person_details, 'title':'Negros'})
        
def add_authorizedPerson_view(request, rs_number):
    init_data = {'header':NegrosRequestHeader.objects.get(pk=rs_number)}
    if request.method == 'POST':
        form = AuthorizedPersonsForm(request.POST, request.FILES, initial=init_data)
        if form.is_valid:
            form.save()
            messages.success(request, "Person Added Successfully")
            return redirect(reverse('Negros'))
        
    form = AuthorizedPersonsForm(initial=init_data)
    return render(request, 'main/actions/add_authorizedPerson.html', {'form':form, 'title':'Negros'})


def list_view_requests(request):
    rs = NegrosRequestHeader.objects.all()
    return render(request, 'main/actions/list_view_request.html', {'rs':rs, 'title':'Negros'})


def edit_item_view(request, rs_id):
    # header=NegrosRequestHeader.objects.get(pk=rs_id)
    item = NegrosRequestItems.objects.get(pk=rs_id)
    
    form = NegrosRequestItemsForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Item Updated Successfully")
        return redirect(reverse(list_view_items))
    else:
        return render(request, 'main/actions/edit_item.html', {'form':form, 'title':'Negros'})

def edit_request_view(request, rs_number):
    rs = NegrosRequestHeader.objects.get(pk=rs_number)
    form = NegrosRequestHeaderForm(request.POST or None, instance=rs)

    if form.is_valid():
        form.save()
        messages.success(request, "Request Updated Successfully")
        return redirect(reverse(list_view_requests))
    else:
        return render(request, 'main/actions/edit_request.html', {'form':form, 'title':'Negros'}) 
 
def edit_authorizedPerson_view(request, rs_number):
    instance_data = AuthorizedPersons(NegrosRequestHeader.objects.get(pk=rs_number))
    if request.method == 'POST':
        form = AuthorizedPersonsForm(
            request.POST,
            request.FILES,
            instance=instance_data
            )
        
        if form.is_valid():
            form.save()
            return redirect(reverse('Negros'))
        
    form = AuthorizedPersonsForm(instance=instance_data)
    return render(request, 'main/actions/add_authorizedPerson.html', {'form':form, 'title':'Negros'})


def list_view_items(request):
    items = NegrosRequestItems.objects.all()
    return render(request, 'main/actions/list_view_items.html', {'items':items, 'title':'Negros'})


def go_back(request):
    referer = request.META.get('HTTP_REFERER')

    return redirect(referer)

def delete_item(request, item_id):
    item = NegrosRequestItems.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Deleted Successfully")
    return redirect(reverse(list_view_items))