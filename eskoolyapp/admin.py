from django.contrib import admin
from eskoolyapp.models import CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE,EMPLOYEE

# Register your models here.
# class TableAdmin(admin.ModelAdmin):
#     list_display=['username','password']

# admin.site.register(Table)
admin.site.register(CLASS)
admin.site.register(SUBJECT)
admin.site.register(ADMISSION)
admin.site.register(INSTITUTECHANGE)
admin.site.register(EMPLOYEE)
