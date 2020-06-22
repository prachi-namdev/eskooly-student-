from django import forms
from eskoolyapp.models import Table,CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE
from django.contrib.auth.models import User

class table(forms.ModelForm):
    class Meta:
        model=Table
        fields='__all__'

class CLASSFORM(forms.ModelForm):
    class Meta:
        model=CLASS
        fields=('name','fees')

class SUBJECTFORM(forms.ModelForm):
    class Meta:
        model=SUBJECT
        # fields=('Subjectname','mark')
        fields='__all__'



# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
class ADMISSIONFORM(forms.ModelForm):
    class Meta:
        model=ADMISSION
        fields=('nmstd','regno','image','mobno','gender','admission_date')
        widgets={
        'nmstd':forms.TextInput(attrs={'placeholder':'Name of student'}),
        'regno':forms.TextInput(attrs={'placeholder':'Registration No.'}),
        'mobno':forms.TextInput(attrs={'placeholder':'Mobile No.'}),
        }

class FATHERFORM(forms.ModelForm):
    class Meta:
        model=ADMISSION
        fields=('fnm','education','occupation','profession','father_mobno','father_income')

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
)
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
