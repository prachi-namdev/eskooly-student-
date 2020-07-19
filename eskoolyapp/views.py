from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from eskoolyapp.models import CLASS,SUBJECT,ADMISSION,INSTITUTECHANGE,EMPLOYEE,ACCOUNTS,BALANCE
from eskoolyapp.forms import CLASSFORM,SUBJECTFORM,ADMISSIONFORM,FATHERFORM,CHANGEFORM,RULESFORM,FEEFORM,MOTHERFORM,BASICEMPFORM,OTHEREMPFORM,INCOMEFORM,EXPENSEFORM,MARKEMPFORM
from django.views.generic import UpdateView,DeleteView,DetailView
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.db.models import Sum
# Create your views here.
# login page
def signin(request):
    return render(request,'eskoolyapp/signin.html');
# base class
def base(request):
    return render(request,'eskoolyapp/base.html');

#dashboard
def dashboard(request):
    return render(request,'eskoolyapp/dashboard.html')
# show all classes
def allclasses(request):
    name=CLASS.objects.all()
    mydict={'name':name}
    return render(request,'eskoolyapp/allclasses.html',context=mydict);
# new class add
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
#edit class
def editclass(request):
    name=CLASS.objects.all()
    mydict={'name':name}
    return render(request,'eskoolyapp/editclass.html',context=mydict);
#update class
class updateclass(UpdateView):
    model=CLASS
    fields='__all__'
    def get_success_url(self):
            return reverse('home')
#delete class
class deleteclass(DeleteView):
    model=CLASS
    def get_success_url(self):
            return reverse('home')
#add subject
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
# show all subject
def showsubject(request):
    subject=SUBJECT.objects.all()
    mydict={'subject':subject}
    return render(request,'eskoolyapp/showsubject.html',context=mydict);
# institute show
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

# student
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

# all student show
def allstudent(request):
    allad=ADMISSION.objects.all()
    mydict={'allad':allad}
    return render(request,'eskoolyapp/allstudent.html',context=mydict)
# delete student
class deletestudent(DeleteView):
    model=ADMISSION
    def get_success_url(self):
            return reverse('index')
#update student
class updatestudent(UpdateView):
    model=ADMISSION
    fields='__all__'
    def get_success_url(self):
        return reverse('index')
# student report
class studentreport(DetailView):
    model=ADMISSION
# student card
def studentcard(request):
    card=ADMISSION.objects.all()
    mydict={'card':card}
    return render(request,'eskoolyapp/studentcard.html',context=mydict)
# student admission letter
def admisletter(request):
   return render(request,'eskoolyapp/admisletter.html')

# def letter(request):
#     return render(request,'eskoolyapp/letter.html')
# student admission letter search
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
#print  student letter
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
# show all empolyee
def allemployee(request):
    employ=EMPLOYEE.objects.all()
    mydict={'employ':employ}
    return render(request,'eskoolyapp/allemployee.html',context=mydict)
#add new employee
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
# update employee
class updateemployee(UpdateView):
    model=EMPLOYEE
    fields='__all__'
    def get_success_url(self):
        return reverse('home1')
# delete employee
class deleteemployee(DeleteView):
    model=EMPLOYEE
    def get_success_url(self):
            return reverse('home1')
# employee report
class employeereport(DetailView):
    model=EMPLOYEE

# add income
def addincome(request,id):
    obj= get_object_or_404(ACCOUNTS,id=id)
    account = ACCOUNTS.objects.all()
    income = INCOMEFORM()
    mydict = {'account': account, 'income': income}
    if request.method == 'POST':
        income = INCOMEFORM(request.POST,request.FILES, instance = obj)
        if income.is_valid():
            obj = income.save()
            obj.save()
            mydict = {'account': account, 'income': income}
        return render(request,'eskoolyapp/dashboard.html')
    else:
        return render(request,'eskoolyapp/add_income.html',context=mydict)
# add expense
def addexpense(request,id):
    obj= get_object_or_404(ACCOUNTS,id=id)
    account = ACCOUNTS.objects.all()
    expense = EXPENSEFORM()
    mydict = {'account': account, 'expense': expense}
    if request.method == 'POST':
        expense = EXPENSEFORM(request.POST,request.FILES, instance = obj)
        if expense.is_valid():
            obj = expense.save()
            obj.save()
            mydict = {'account': account, 'expense': expense}

            return render(request,'eskoolyapp/dashboard.html')
    else:
        return render(request,'eskoolyapp/add_expense.html',context=mydict)

# class account_statement(DetailView):
#     model = BALANCE
# a/c statement
def account_statement(request):
    balance=ACCOUNTS.objects.all()
    debit=ACCOUNTS.objects.aggregate(Debit=Sum('expense_amount'))
    credit=ACCOUNTS.objects.aggregate(Credit=Sum('income_amount'))
    # net_balance = income_amount-expense_amount
    mydict={'balance':balance,'debit':debit,'credit':credit}
    return render(request,'eskoolyapp/balance_detail.html',context=mydict)

    # if request.method == 'GET':
    #     query= request.GET.get('q')
    #
    #     submitbutton= request.GET.get('submit')
    #
    #     if query is not None:
    #         lookups= Q(date_income__icontains=query) | Q(date_expense__icontains=query)
    #
    #         results= ACCOUNTS.objects.filter(lookups).distinct()
    #
    #         context={'results': results,
    #                  'submitbutton': submitbutton}
    #
    #         return render(request, 'eskoolyapp/balance_detail.html', context)
    #
    #     else:
    #         return render(request, 'eskoolyapp/balance_detail.html')


class deleteaccount(DeleteView):
    model=BALANCE
    def get_success_url(self):
            return reverse('home2')

def student_mark_attendence(request):
    # template_name = 'eskoolyapp/mark_student_attendence.html'
    # student=ADMISSION.objects.all()
    # query = request.GET.get('q', '')
    # if query:
    #     # query example
    #     results = ADMISSION.objects.filter(classnm__icontains=query).distinct()
    # else:
    #     results = []
    # return render(
    #     request, template_name, {'results': results,'student':student})

    student=ADMISSION.objects.all()
    mydict={'student':student}
    return render(request,'eskoolyapp/mark_student_attendence.html',context=mydict)
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(classnm__icontains=query) | Q(classnm__icontains=query)

            results= ADMISSION.objects.filter(lookups).distinct()

            context={'results': results,'submitbutton': submitbutton}

            return render(request, 'eskoolyapp/mark_student_attendence.html', context)

        else:
            return render(request, 'eskoolyapp/mark_student_attendence.html')

    else:
       return render(request,'eskoolyapp/mark_student_attendence.html')



def employee_mark_attendence(request,id):
    obj= get_object_or_404(ACCOUNTS,id=id)
    mark=EMPLOYEE.objects.all()
    emp = MARKEMPFORM()
    mydict={'mark':mark,'emp':emp}
    # return render(request,'eskoolyapp/mark_employee_attendence.html',context=mydict)
    if request.method == 'POST':
        emp = MARKEMPFORM(request.POST,request.FILES, instance = obj)
        if emp.is_valid():
            obj = emp.save()
            obj.save()
            mydict = {'mark':mark,'emp':emp}
        return render(request,'eskoolyapp/dashboard.html')
    else:
        return render(request,'eskoolyapp/mark_employee_attendence.html',context=mydict)

def attendance_sheet(request):
    # if request.method == 'GET':
    #     query= request.GET.get('q')
    #
    #     submitbutton= request.GET.get('submit')
    #
    #     if query is not None:
    #         lookups= Q(classnm__icontains=query) | Q(classnm__icontains=query)
    #
    #         results= ADMISSION.objects.filter(lookups).distinct()
    #
    #         context={'results': results,
    #                  'submitbutton': submitbutton}
    #
    #         return render(request, 'eskoolyapp/attendance_sheet.html', context)
    #
    #     else:
    #         return render(request, 'eskoolyapp/attendance_sheet.html')
    #
    # else:
    #     return render(request, 'eskoolyapp/attendance_sheet.html',context)
    attend=ADMISSION.objects.all()
    mydict={'attend':attend}
    return render(request,'eskoolyapp/attendance_sheet.html',context=mydict)

def emp_attend_report(request):
    emp_report=EMPLOYEE.objects.all()
    mydict={'emp_report':emp_report}
    return render(request,'eskoolyapp/emp_attend_report.html',context=mydict)

def student_attend_report(request):
    student_report=ADMISSION.objects.all()
    mydict={'student_report':student_report}
    return render(request,'eskoolyapp/studmark_attend_report.html',context=mydict)

def today_attend_report(request):
    today_report=ADMISSION.objects.all()
    mydict={'today_report':today_report}
    return render(request,'eskoolyapp/today_attend_report.html',context=mydict)
