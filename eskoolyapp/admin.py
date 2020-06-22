from django.contrib import admin
from eskoolyapp.models import Table,CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE
# Register your models here.
# class TableAdmin(admin.ModelAdmin):
#     list_display=['username','password']

admin.site.register(Table)
admin.site.register(CLASS)
admin.site.register(SUBJECT)
admin.site.register(ADMISSION)
admin.site.register(INSTITUTECHANGE)
