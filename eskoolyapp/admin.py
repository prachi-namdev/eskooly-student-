from django.contrib import admin
from eskoolyapp.models import CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE,EMPLOYEE,ACCOUNTS,BALANCE

# Register your models here.
# class TableAdmin(admin.ModelAdmin):
#     list_display=['username','password']

# admin.site.register(Table)
admin.site.register(CLASS)          # class model register
admin.site.register(SUBJECT)        # subject model register
admin.site.register(ADMISSION)      # admission/student model register
admin.site.register(INSTITUTECHANGE)  # Institute_change model register
admin.site.register(EMPLOYEE)        # employee model register
admin.site.register(ACCOUNTS)        # account model register
admin.site.register(BALANCE)        # balance model register 
