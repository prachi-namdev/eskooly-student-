from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from eskoolyapp.models import CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE,EMPLOYEE
from eskoolyapp.forms import CLASSFORM,SUBJECTFORM,ADMISSIONFORM,FATHERFORM,CHANGEFORM,RULESFORM,FEEFORM,MOTHERFORM,BASICEMPFORM,OTHEREMPFORM
from django.views.generic import UpdateView,DeleteView,DetailView
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
# Create your views here.

def signin(request):

    return render(request,'eskoolyapp/signin.html');

def base(request):
    return render(request,'eskoolyapp/base.html');

def allclasses(request):
    name=CLASS.objects.all()
    mydict={'name':name}
    return render(request,'eskoolyapp/allclasses.html',context=mydict);

def addnewclass(request):
    classform=CLASSFORM()
    mydict={'classform':classform}
    if request.method == 'POST':
        classform=CLASSFORM(request.POST,request.FILES)
        if classform.is_valid():
            data=classform.save(commit=False)
            data.author=request.user
            data.save()
            mydict.update({'msg':'Add New Class'})
    return render(request,'eskoolyapp/addnewclass.html',context=mydict);

def editclass(request):
    name=CLASS.objects.all()
    mydict={'name':name}
    return render(request,'eskoolyapp/editclass.html',context=mydict);

class updateclass(UpdateView):
    model=CLASS
    fields='__all__'
    def get_success_url(self):
            return reverse('home')

class deleteclass(DeleteView):
    model=CLASS
    def get_success_url(self):
            return reverse('home')

def addsubject(request):
    subjectform=SUBJECTFORM()
    mydict={'subjectform':subjectform}
    if request.method == 'POST':
        subjectform=SUBJECTFORM(request.POST,request.FILES)
        if subjectform.is_valid():
            data=subjectform.save(commit=False)
            # data.author=request.user
            data.save()
            mydict.update({'msg':'Add subject successful'})
    return render(request,'eskoolyapp/addsubject.html',context=mydict);

def showsubject(request):
    subject=SUBJECT.objects.all()
    mydict={'subject':subject}
    return render(request,'eskoolyapp/showsubject.html',context=mydict);

def view_institute_info(request,id):
    obj= get_object_or_404(INSTITUTECHANGE,id=id)
    obj1= get_object_or_404(INSTITUTECHANGE,id=id)
    obj2= get_object_or_404(INSTITUTECHANGE,id=id)
    inst_info = INSTITUTECHANGE.objects.all()
    institute_info_form = CHANGEFORM()
    rules_form = RULESFORM()
    fees_form = FEEFORM()
    mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info, 'rules_form':rules_form, 'fees_form':fees_form}
    if request.method == 'POST':
        institute_info_form = CHANGEFORM(request.POST,request.FILES, instance = obj)
        rules_form = RULESFORM(request.POST, instance = obj1)
        fees_form = FEEFORM(request.POST, instance = obj2)
        if institute_info_form.is_valid():
            obj = institute_info_form.save()
            obj.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}
        if rules_form.is_valid():
            obj1 = rules_form.save()
            obj1.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}
        if fees_form.is_valid():
            obj2 = fees_form.save()
            obj2.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}

    return render(request,'EskoolyApp/instituteinfo.html', context = mydict)


def admission(request,id):
    obj= get_object_or_404(ADMISSION,id=id)
    obj1= get_object_or_404(ADMISSION,id=id)
    obj2= get_object_or_404(ADMISSION,id=id)
    ad = ADMISSION.objects.all()
    mission = ADMISSIONFORM()
    mission2 = FATHERFORM()
    mission3 = MOTHERFORM()
    mydict = {'mission': mission, 'ad': ad, 'mission2':mission2, 'mission3':mission3}
    if request.method == 'POST':
        mission = ADMISSIONFORM(request.POST,request.FILES, instance = obj)
        rules_form = FATHERFORM(request.POST, instance = obj1)
        fees_form = MOTHERFORM(request.POST, instance = obj2)
        if mission.is_valid():
            obj = mission.save()
            obj.save()
            mydict = {'mission': mission, 'ad': ad,'mission2':mission2, 'mission3':mission3}
        if mission2.is_valid():
            obj1 = mission2.save()
            obj1.save()
            mydict = {'mission': mission, 'ad': ad,'mission2':mission2, 'mission3':mission3}
        if mission3.is_valid():
            obj2 = mission3.save()
            obj2.save()
            mydict = {'mission': mission, 'ad': ad,'mission2':mission2, 'mission3':mission3}

    return render(request,'eskoolyapp/admission.html', context = mydict)


def allstudent(request):
    allad=ADMISSION.objects.all()
    mydict={'allad':allad}
    return render(request,'eskoolyapp/allstudent.html',context=mydict)

class deletestudent(DeleteView):
    model=ADMISSION
    def get_success_url(self):
            return reverse('index')

class updatestudent(UpdateView):
    model=ADMISSION
    fields='__all__'
    def get_success_url(self):
        return reverse('index')

class studentreport(DetailView):
    model=ADMISSION
    
def studentcard(request):
    card=ADMISSION.objects.all()
    mydict={'card':card}
    return render(request,'eskoolyapp/studentcard.html',context=mydict)

def admisletter(request):
   return render(request,'eskoolyapp/admisletter.html')

def letter(request):
    return render(request,'eskoolyapp/letter.html')

def StudentAdmissionLetter(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(regno__icontains=query) | Q(nmstd__icontains=query)

            results= ADMISSION.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'EskoolyApp/admission_letter.html', context)

        else:
            return render(request, 'EskoolyApp/admission_letter.html')

    else:
        return render(request, 'EskoolyApp/admission_letter.html')

def PrintAdmissionLetter(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(regno__icontains=query) | Q(nmstd__icontains=query)

            results= ADMISSION.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'EskoolyApp/print_admission_letter.html', context)

        else:
            return render(request, 'EskoolyApp/print_admission_letter.html')

    else:
        return render(request, 'EskoolyApp/print_admission_letter.html')

def allemployee(request):
    employ=EMPLOYEE.objects.all()
    mydict={'employ':employ}
    return render(request,'eskoolyapp/allemployee.html',context=mydict)

def addemployee(request,id):
    obj= get_object_or_404(EMPLOYEE,id=id)
    obj1= get_object_or_404(EMPLOYEE,id=id)
    obj2= get_object_or_404(EMPLOYEE,id=id)
    emp = EMPLOYEE.objects.all()
    e1 = BASICEMPFORM()
    e2 = OTHEREMPFORM()
    mydict = {'emp': emp, 'e1': e1, 'e2':e2}
    if request.method == 'POST':
        e1 = BASICEMPFORM(request.POST,request.FILES, instance = obj)
        e2 = OTHEREMPFORM(request.POST, instance = obj1)
        if e1.is_valid():
            obj = e1.save()
            obj.save()
            mydict = {'emp': emp, 'e1': e1, 'e2':e2}
        if e2.is_valid():
            obj1 = e2.save()
            obj1.save()
            mydict = {'emp': emp, 'e1': e1, 'e2':e2}

    return render(request,'eskoolyapp/add_employee.html',context=mydict)

class updateemployee(UpdateView):
    model=EMPLOYEE
    fields='__all__'
    def get_success_url(self):
        return reverse('home1')

class deleteemployee(DeleteView):
    model=EMPLOYEE
    def get_success_url(self):
            return reverse('home1')

class employeereport(DetailView):
    model=EMPLOYEE
