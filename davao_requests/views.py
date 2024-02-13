from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.http.response import HttpResponse
from .models import DavaoRequestHeader, DavaoRequestItems, AuthorizedPersons, Monitoring
from .forms import DavaoRequestHeaderForm, DavaoRequestItemsForm, AuthorizedPersonsForm, MonitoringForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# timezone.now().year

# Create your views here.
person_form = AuthorizedPersonsForm

def dashboard(request):
    # monitoringData = DavaoRequestItems.objects.all()
    if request.user.is_authenticated:
        monitoringData = Monitoring.objects.prefetch_related('header')
        
        return render(request, 'main/actions/dashboard.html', {'title':'Davao', 'data':monitoringData})
    else:
        return redirect('login')

def add_request_view(request):
    if request.user.is_authenticated:
        
    
        if request.method == 'POST':
            form = DavaoRequestHeaderForm(request.POST, instance=DavaoRequestHeader(user=User.objects.get(pk=request.user.id)))
            if form.is_valid:
                rs_number = request.POST['rs_number']
                form.save()
                messages.success(request, "Request Added Successfully")
                return redirect(reverse('davao_add_authorizedPerson', kwargs={'rs_number':rs_number}))
            else:
                print(form.errors)
            
        rs_number = f"DVO{timezone.now().year}-"
        try:
            idx = DavaoRequestHeader.objects.all()
            rs_number += str(len(idx)+1).zfill(3)
        except:
            rs_number += str(1).zfill(3)

        form = DavaoRequestHeaderForm(initial={'rs_number':rs_number})
        return render(request, 'main/actions/add_request.html', {'form':form,'title':'Davao'})
    else:
        return redirect('login')

def monitoringForm(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            try:
                instance = Monitoring.objects.get(header=request.POST['header'])
                form = MonitoringForm(request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    return redirect(reverse(dashboard))
                else:
                    return HttpResponse('MonitoringForm Function Error: Level 1')
            except:
                return HttpResponse('MonitoringForm Function Error: Level 2')
        else:
            form = MonitoringForm()
            return render(request, 'main/actions/modal_update_monitoring.html', {'form':form})
    else:
        return redirect('login')
    

def add_items_view(request, rs_number):
    if request.user.is_authenticated:
            
        init_data = {'header':rs_number}
        items = DavaoRequestItems.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
        # items[0].
        if request.method == "POST":
            form = DavaoRequestItemsForm(request.POST)
            if form.is_valid:
                form.save()
                messages.success(request, "Item Addedd Successfully")
            
        form = DavaoRequestItemsForm(initial=init_data)
        return render(request, 'main/actions/add_items.html', {'form':form, 'items':items, 'title':'Davao'})
    else:
        return redirect('login')
    

def add_itemsRequest_view(request, rs_number):
    if request.user.is_authenticated:
            
        init_data = {'header':rs_number}
        # items[0].
        if request.method == "POST":
            form = DavaoRequestItemsForm(request.POST)
            if form.is_valid:
                form.save()
                messages.success(request, "Item Addedd Successfully")
            
        form = DavaoRequestItemsForm(initial=init_data)
        return redirect(reverse(list_viewRequest_items, kwargs={'rs_number':rs_number}))
    else:
        return redirect('login')

def rs_view(request, rs_number):
    if request.user.is_authenticated:
                
        header = DavaoRequestHeader.objects.get(pk=rs_number)
        items = DavaoRequestItems.objects.filter(header=header)
        total = items.aggregate(amount_sum=Sum('amount'))['amount_sum']
        persons = AuthorizedPersons.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
        person_details = {}
        for person in persons:
            name = person.name
            person_details[person.title.replace(" ","_")] = (name, person.signature)

        return render(request, 'main/actions/rsSlip.html', {'header':header, 'items':items, 'fields':list(range(1,16-len(items)+1)), 'total':total, 'persons':person_details, 'title':'Davao'})
    else:
        return redirect('login')
    

def add_authorizedPerson_view(request, rs_number):
    if request.user.is_authenticated:
                
        # global person_form
        init_data = {'header':DavaoRequestHeader.objects.get(pk=rs_number)}
        persons = AuthorizedPersons.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
        if request.method == 'POST':
            form = AuthorizedPersonsForm(request.POST, request.FILES, initial=init_data)
            if form.is_valid:
                form.save()
                
                messages.success(request, "Person Added Successfully")
                return redirect(reverse('davao_add_authorizedPerson', kwargs={'rs_number':rs_number}))
            
        form = AuthorizedPersonsForm(initial=init_data)

        if len(persons) == len(AuthorizedPersonsForm.Meta.TITLE_CHOICES.keys()):
            return redirect(reverse('davao_add_items', kwargs={'rs_number':rs_number}))
        else:
            return render(request, 'main/actions/add_authorizedPerson.html', {'form':form, 'persons':persons, 'person_form':person_form,'title':'Davao'})
    else:
        return redirect('login')

def list_view_requests(request):
    if request.user.is_authenticated:
                    
        rs = DavaoRequestHeader.objects.all()
        return render(request, 'main/actions/list_view_request.html', {'rs':rs, 'title':'Davao'})
    else:
        return redirect('login')
    

def edit_item_view(request, rs_id):
    if request.user.is_authenticated:
            
        # header=DavaoRequestHeader.objects.get(pk=rs_id)
        item = DavaoRequestItems.objects.get(pk=rs_id)
        
        form = DavaoRequestItemsForm(request.POST or None, instance=item) 
        if form.is_valid():
            form.save()
            messages.success(request, "Item Updated Successfully")

            return redirect(reverse(list_viewRequest_items, kwargs={'rs_number':item.header.rs_number}))
        else:
            return render(request, 'main/actions/edit_item.html', {'form':form, 'title':'Davao'})
    else:
        return redirect('login')
    

def edit_item_listview(request, rs_id):
    if request.user.is_authenticated:
        # header=DavaoRequestHeader.objects.get(pk=rs_id)
        item = DavaoRequestItems.objects.get(pk=rs_id)

        form = DavaoRequestItemsForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Updated Successfully")
            return redirect(reverse(add_items_view, kwargs={'rs_number'}))
        else:
            return render(request, 'main/actions/edit_item.html', {'form':form, 'title':'Davao'})
    else:
        return redirect('login')

def edit_request_view(request, rs_number):
    if request.user.is_authenticated:
                
        rs = DavaoRequestHeader.objects.get(pk=rs_number)
        form = DavaoRequestHeaderForm(request.POST or None, instance=rs)

        if form.is_valid():
            form.save()
            messages.success(request, "Request Updated Successfully")
            return redirect(reverse(list_view_requests))
        else:
            return render(request, 'main/actions/edit_request.html', {'form':form, 'title':'Davao'}) 
    else:
        return redirect('login')

def edit_authorizedPerson_view(request, person_id):
    if request.user.is_authenticated:
            
        instance_data = AuthorizedPersons.objects.get(pk=person_id)
        if request.method == 'POST':
            form = AuthorizedPersonsForm(
                request.POST,
                request.FILES,
                instance=instance_data,
                )
            
            if form.is_valid():
                form.save()
                return redirect(reverse('davao'))
            
        form = AuthorizedPersonsForm(instance=instance_data)
        return render(request, 'main/actions/edit_authorizedPerson.html', {'form':form, 'title':'Davao'})
    else:
        return redirect('login')

def delete_person(request, person_id):
    if request.user.is_authenticated:
                
        person = AuthorizedPersons.objects.get(pk=person_id)
        person.delete()
        messages.success(request, "Person Deleted Successfully")
        return redirect(reverse('davao_add_authorizedPerson', kwargs={'rs_number':person.header.rs}))
    else:
        return redirect('login')


def list_view_persons(request):
    if request.user.is_authenticated:
        persons = AuthorizedPersons.objects.all()
        return render(request, 'main/actions/list_view_persons.html', {'persons':persons, 'title':'Davao'})
    else:
        return redirect('login')


def list_view_items(request):
    if request.user.is_authenticated:        
        items = DavaoRequestItems.objects.all()
        return render(request, 'main/actions/list_view_items.html', {'items':items, 'title':'Davao'})
    else:
        return redirect('login')

def list_viewRequest_items(request, rs_number):
    items = DavaoRequestItems.objects.filter(header=DavaoRequestHeader.objects.get(pk=rs_number))
    return render(request, 'main/actions/list_viewRequest_items.html', {'data':items, 'title':'Davao'})

def go_back(request):
    if request.user.is_authenticated:
        return redirect('login')
    
    referer = request.META.get('HTTP_REFERER')

    return redirect(referer)


def delete_item(request, item_id):
    if request.user.is_authenticated:    
        item = DavaoRequestItems.objects.get(pk=item_id)
        item.delete()
        messages.success(request, "Deleted Successfully")
        return redirect(reverse(list_view_items))
    else:
        return redirect('login')
    
def delete_request(request, rs_number):
    if request.user.is_authenticated:    
        item = DavaoRequestHeader.objects.get(pk=rs_number)
        item.delete()
        messages.success(request, "Deleted Successfully")
        return redirect(reverse(list_view_requests))
    else:
        return redirect('login')


def list_view_report(request):
    if request.user.is_authenticated:    
        req = DavaoRequestHeader.objects.all()
        return render(request, 'main/actions/print_reports.html', {'req':req, 'title':'Davao'})
    else:
        return redirect('login')

def get_items_data(request):
    if request.user.is_authenticated:    
        items = DavaoRequestItems.objects.all()
        labels = [item.description for item in items]
        values = [item.amount for item in items]

        data = {
            'dataset':{'values':values, 'labels':labels, 'color':'blue'},
            'title':'Example Bar Chart',
            'noY':True,
            'height':'300px',
            'width':'500px',
            'background':'#FFFFFF',
            'shadowDepth':'1'
        }

        return JsonResponse(data)
    else:
        return redirect('login')

def monitoring_form_delivery_date(request):
    pass