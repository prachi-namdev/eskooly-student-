from django.db import models
from django.contrib.auth.models import User
from datetime import date

#class model fields
class CLASS(models.Model):
    name=models.CharField(max_length=50)
    fees=models.IntegerField()
    def __str__(self):
        return self.name

#subject model fields
class SUBJECT(models.Model):
    Subjectname=models.CharField(max_length=30)
    mark=models.IntegerField()
    classnm=models.ForeignKey(CLASS,on_delete=models.CASCADE,default="")
    def __str__(self):
        return self.Subjectname

# student model fields
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
#status
CHOICES=[('P','P'),
         ('L','L'),
         ('A','A')]
class ADMISSION(models.Model):
    nmstd=models.CharField(max_length=30)
    regno=models.IntegerField()
    classnm=models.ForeignKey(CLASS,on_delete=models.CASCADE,default="")
    image=models.FileField(upload_to="images/",null=True,blank=True)
    admission_date=models.DateField()
    mobno=models.IntegerField()
    birthdate=models.DateField(null=True, blank=True)
    discount = models.IntegerField()
    fnm=models.CharField(max_length=30)
    education=models.CharField(max_length=10)
    occupation=models.CharField(max_length=30)
    profession=models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES, null=True, blank=True)
    os=models.CharField(max_length=30)
    osc=models.CharField(max_length=30)
    Previous_school=models.CharField(max_length=30)
    Total_children=models.IntegerField(null=True, blank=True)
    father_income=models.FloatField(null=True, blank=True)
    mother_income=models.FloatField(null=True, blank=True)
    mother_profession=models.CharField(max_length=30,null=True, blank=True)
    mother_occupation=models.CharField(max_length=30,null=True, blank=True)
    mother_education=models.CharField(max_length=50,null=True, blank=True)
    mother_mobno=models.IntegerField(null=True, blank=True)
    mothername=models.CharField(max_length=30,null=True, blank=True)
    father_mobno=models.IntegerField(null=True, blank=True)
    std_id=models.IntegerField()
    status =models.CharField(choices=CHOICES, max_length=128)
    def __str__(self):
        return self.nmstd

#institute model fields
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
    ("Argentina","Argentina"),
    ("Armenia","Armenia"),
    ("Australia","Australia"),
    ("Austria","Austria"),
    ("ind","INDIA"),
)
class INSTITUTECHANGE(models.Model):
    Institute_name = models.CharField(max_length=50)
    target_line=models.CharField(max_length=100)
    logo=models.FileField(upload_to='images/')
    phone=models.IntegerField()
    website=models.URLField(max_length=150)
    address=models.CharField(max_length=80)
    location=models.CharField(max_length=10,choices=LOCATION)
    rules=models.TextField(max_length=1000,default='aaaaavbbbbbbbvccccc')
    admission_fee=models.IntegerField(default="")
    registration_fee=models.IntegerField()
    art_material=models.CharField(max_length=30)
    transport=models.CharField(max_length=50)
    book=models.CharField(max_length=100)
    uniform=models.CharField(max_length=100)
    fine=models.IntegerField()
    others=models.CharField(max_length=100)
    def __str__(self):
        return self.Institute_name
#
# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
# employee model fields
bloodgroup_choices = (('apos', 'A+'),
        ('aneg', 'A-'),
        ('bpos', 'B+'),
        ('bneg', 'B-'),
        ('opos', 'O+'),
        ('oneg', 'O-'),
        ('abpos', 'AB+'),
        ('abneg', 'AB-'),
        ('unspecified', '-'))

CHOICES=[('P','P'),
         ('L','L'),
         ('A','A')]
class EMPLOYEE(models.Model):
    name_of_employee = models.CharField(max_length=30)
    joining_date = models.DateField(null=True, blank=True)
    mobile_no = models.IntegerField(null=True, blank=True)
    employee_type = models.CharField(max_length=60)
    monthly_salary = models.FloatField(null=True,blank=True)
    image = models.FileField(upload_to="images/",null=True,blank=True)
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES, null=True,blank=True)
    father_name = models.CharField(max_length=30)
    education = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    bloodgroup = models.CharField(choices=bloodgroup_choices,max_length=11, default='-', blank=True)
    emp_id = models.IntegerField()
    status =models.CharField(choices=CHOICES, max_length=128)
    def __str__(self):
        return self.education

# account model fields
class ACCOUNTS(models.Model):
    date_income=models.DateField()
    income_discription=models.CharField(max_length=5000)
    income_amount=models.FloatField(default='0')
    date_expense=models.DateField()
    expense_discription=models.CharField(max_length=5000)
    expense_amount=models.FloatField(default='0')
# a/c statement fields
class BALANCE(models.Model):
    serial_no=models.IntegerField()
    date=models.DateField()
    description=models.CharField(max_length=5000)
    debit=models.FloatField()
    credit=models.FloatField()
    net_balance=models.FloatField()
