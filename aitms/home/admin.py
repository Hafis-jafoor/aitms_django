from django.contrib import admin

from . models import Enquiry_contacts, Vistor_contacts, Parscore
# Register your models here.

class EnquiryContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'contact_phone', 'contact_subject', 'contact_message')

class VistorContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'contact_phone', 'contact_subject', 'contact_message')

class ParscoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'Parscore_student_name', 'Parscore_school_name', 'Parscore_sector', 'Parscore_phone', 'Parscore_email', 'Parscore_location', 'Parscore_career', 'Parscore_career_other')

admin.site.register(Enquiry_contacts, EnquiryContactAdmin)
admin.site.register(Vistor_contacts, VistorContactAdmin)
admin.site.register(Parscore, ParscoreAdmin)
