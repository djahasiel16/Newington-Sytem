from django.contrib import admin
from .models import DavaoRequestHeader, DavaoRequestItems, AuthorizedPersons, Monitoring

var_models = DavaoRequestHeader, DavaoRequestItems, AuthorizedPersons, Monitoring
# Register your models here.
for var_model in var_models:
    admin.site.register(var_model)