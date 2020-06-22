from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Table(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=10)
    # def __str__(self):
    #     return self.username
class CLASS(models.Model):
    name=models.CharField(max_length=50)
    fees=models.IntegerField()
    def __str__(self):
        return self.name

class SUBJECT(models.Model):
    Subjectname=models.CharField(max_length=30)
    mark=models.IntegerField()
    classnm=models.ForeignKey(CLASS,on_delete=models.CASCADE)
    def __str__(self):
        return self.Subjectname

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class ADMISSION(models.Model):
    nmstd=models.CharField(max_length=30)
    regno=models.IntegerField()
    # class_name_id=models.ForeignKey(CLASS,on_delete = models.CASCADE)
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
    def __str__(self):
        return self.nmstd

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
