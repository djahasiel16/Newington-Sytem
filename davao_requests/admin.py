from django.contrib import admin
from .models import DavaoRequestHeader, DavaoRequestItems, AuthorizedPersons

# Register your models here.
admin.site.register(DavaoRequestHeader)
admin.site.register(DavaoRequestItems)
admin.site.register(AuthorizedPersons)