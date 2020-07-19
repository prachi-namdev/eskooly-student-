from django import forms
from eskoolyapp.models import CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE,EMPLOYEE,ACCOUNTS
from django.contrib.auth.models import User

# class table(forms.ModelForm):
#     class Meta:
#         model=Table
#         fields='__all__'

# class model form Create
class CLASSFORM(forms.ModelForm):
    class Meta:
        model=CLASS
        fields=('name','fees')
        widgets={
        'name':forms.TextInput(attrs={'placeholder':'Name'}),
        'fees':forms.TextInput(attrs={'placeholder':'Fees'}),
        }
# subject model form Create
class SUBJECTFORM(forms.ModelForm):
    class Meta:
        model=SUBJECT
        # fields=('Subjectname','mark')
        fields='__all__'


# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
# student form create
class ADMISSIONFORM(forms.ModelForm):
    class Meta:
        model=ADMISSION
        fields=('nmstd','regno','image','mobno','gender','admission_date','classnm')
        widgets={
        'nmstd':forms.TextInput(attrs={'placeholder':'Name of student'}),
        'regno':forms.TextInput(attrs={'placeholder':'Registration No.'}),
        'mobno':forms.TextInput(attrs={'placeholder':'Mobile No.'}),
        'mobno':forms.TextInput(attrs={'placeholder':'Mobile No.'}),
        }

# in student father form create
class FATHERFORM(forms.ModelForm):
    class Meta:
        model=ADMISSION
        fields=('fnm','education','occupation','profession','father_mobno','father_income')

# in student mother form create
class MOTHERFORM(forms.ModelForm):
    class Meta:
        model=ADMISSION
        fields=('mothername','mother_education','mother_mobno','mother_occupation','mother_profession')


LOCATION =(
    ("us", "United States"),
    ("uk", "United Kingdom"),
    ("afg","Afghanistan"),
    ("albania","Albania"),
    ("Algeria","Algeria"),
    ("as","American Samoa"),
    ("Andorra","Andorra"),
    ("Angola","Angola"),
    ("Anguilla","Anguilla"),
    ("Antarctica","Antarctica"),
    ("ab","Antigua and Barbuda"),
    ("ind","INDIA"),
)
#Institute form create
class CHANGEFORM(forms.ModelForm):
    class Meta:
        model=INSTITUTECHANGE
        fields=('Institute_name','target_line','logo','phone','website','address','location')
        widgets={
        'Institute_name':forms.TextInput(attrs={'placeholder':'Institute name'}),
        }

class RULESFORM(forms.ModelForm):
    class Meta:
        model=INSTITUTECHANGE
        fields=('rules',)

class FEEFORM(forms.ModelForm):
    class Meta:
        model=INSTITUTECHANGE
        fields=('admission_fee','registration_fee','art_material','transport','book','uniform','fine','others')

# employee form create
class BASICEMPFORM(forms.ModelForm):
    class Meta:
        model=EMPLOYEE
        fields= ('name_of_employee','joining_date','employee_type','monthly_salary','image','mobile_no')

class OTHEREMPFORM(forms.ModelForm):
    class Meta:
        model=EMPLOYEE
        fields=('father_name','education','date_of_birth','email','bloodgroup','address')

# account form Create
class INCOMEFORM(forms.ModelForm):
    class Meta:
        model = ACCOUNTS
        fields=['date_income','income_discription','income_amount']
        widgets={
        'income_discription':forms.TextInput(attrs={'placeholder':'Income Description'}),
        'income_amount':forms.TextInput(attrs={'placeholder':'Income Amount'}),
        }

class EXPENSEFORM(forms.ModelForm):
    class Meta:
        model = ACCOUNTS
        fields=('date_expense','expense_discription','expense_amount')
        widgets={
        'expense_discription':forms.TextInput(attrs={'placeholder':'Expense Description'}),
        'expense_amount':forms.TextInput(attrs={'placeholder':'Expense Amount'}),
        }

class MARKEMPFORM(forms.ModelForm):
    class Meta:
        model = EMPLOYEE
        fields=('emp_id','name_of_employee','father_name','employee_type','status')
