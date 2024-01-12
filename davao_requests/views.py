from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.http.response import HttpResponse
from .models import DavaoRequestHeader, DavaoRequestItems, AuthorizedPersons
from .forms import DavaoRequestHeaderForm, DavaoRequestItemsForm, AuthorizedPersonsForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# timezone.now().year

# Create your views here.
def home(request):
    return render(request, 'davao_requests/home.html')


def add_request_view(request):
    if request.method == 'POST':
        form = DavaoRequestHeaderForm(request.POST, instance=DavaoRequestHeader(user=User.objects.get(pk=request.user.id)))
        if form.is_valid:
            rs_number = request.POST['rs_number']
            form.save()
            messages.success(request, "Request Added Successfully")
            return redirect(reverse('davao_add_items', kwargs={'rs_number':rs_number}))
        
    rs_number = f"DVO{timezone.now().year}-"
    try:
        idx = DavaoRequestHeader.objects.all()
        rs_number += str(len(idx)+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = DavaoRequestHeaderForm(initial={'rs_number':rs_number})
    return render(request, 'davao_requests/add_request.html', {'form':form})

def add_items_view(request, rs_number):
    init_data = {'header':rs_number}
    items = DavaoRequestItems.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
    if request.method == "POST":
        form = DavaoRequestItemsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Item Addedd Successfully")
        
    form = DavaoRequestItemsForm(initial=init_data)
    return render(request, 'davao_requests/add_items.html', {'form':form, 'items':items})

def rs_view(request, rs_number):
    header = DavaoRequestHeader.objects.get(pk=rs_number)
    items = DavaoRequestItems.objects.filter(header=header)
    total = items.aggregate(amount_sum=Sum('amount'))['amount_sum']
    persons = AuthorizedPersons.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
    person_details = {}
    for person in persons:
        name = ' '.join([person.firstname, "" if str(person.middle_initial) == 'None' else person.middle_initial+'.', person.lastname])
        person_details[person.title.replace(" ","_")] = (name, person.signature)
        print(person_details)

    return render(request, 'davao_requests/rsSlip.html', {'header':header, 'items':items, 'fields':list(range(1,16-len(items)+1)), 'total':total, 'persons':person_details})
        
def add_authorizedPerson_view(request, rs_number):
    init_data = {'header':DavaoRequestHeader.objects.get(pk=rs_number)}
    if request.method == 'POST':
        form = AuthorizedPersonsForm(request.POST, request.FILES, initial=init_data)
        if form.is_valid:
            form.save()
            messages.success(request, "Person Added Successfully")
            return redirect(reverse('davao'))
        
    form = AuthorizedPersonsForm(initial=init_data)
    return render(request, 'davao_requests/add_authorizedPerson.html', {'form':form})


def list_view_requests(request):
    rs = DavaoRequestHeader.objects.all()
    return render(request, 'davao_requests/list_view_request.html', {'rs':rs})


def edit_item_view(request, rs_id):
    # header=DavaoRequestHeader.objects.get(pk=rs_id)
    item = DavaoRequestItems.objects.get(pk=rs_id)
    
    form = DavaoRequestItemsForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Item Updated Successfully")
        return redirect(reverse(list_view_items))
    else:
        return render(request, 'davao_requests/edit_item.html', {'form':form})
    
def edit_authorizedPerson_view(request, rs_number):
    instance_data = AuthorizedPersons(DavaoRequestHeader.objects.get(pk=rs_number))
    if request.method == 'POST':
        form = AuthorizedPersonsForm(
            request.POST,
            request.FILES,
            instance=instance_data
            )
        
        if form.is_valid():
            form.save()
            return redirect(reverse('davao'))
        
    form = AuthorizedPersonsForm(instance=instance_data)
    return render(request, 'davao_requests/add_authorizedPerson.html', {'form':form})


def list_view_items(request):
    items = DavaoRequestItems.objects.all()
    return render(request, 'davao_requests/list_view_items.html', {'items':items})


def go_back(request):
    referer = request.META.get('HTTP_REFERER')

    return redirect(referer)

def delete_item(request, item_id):
    item = DavaoRequestItems.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Deleted Successfully")
    return redirect(reverse(list_view_items))