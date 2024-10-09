from django.contrib import admin
from .models import Contact, Enquiry

class ContactAdmin(admin.ModelAdmin):
    pass

class EnquiryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
