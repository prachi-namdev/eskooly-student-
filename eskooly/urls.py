"""eskooly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from eskoolyapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signin),
    path('base/',views.base),
    path('accounts/',include('django.contrib.auth.urls')),

    # dashboard
    path('dashboard/',views.dashboard),
    # class module start
    path('allclasses/',views.allclasses),
    path('addnewclass/',views.addnewclass),
    path('editclass/',views.editclass,name='home'),
    path('update/<pk>',views.updateclass.as_view()),
    path('delete/<pk>',views.deleteclass.as_view()),
    path('showsubject/',views.showsubject),
    path('addsubject/',views.addsubject),
    # class module close

    # path('Instituteinfo/',views.Instituteinfo),

    # student module open
    path('allstudent/',views.allstudent,name='index'),
    path('admission/<id>',views.admission),
    path('studentupdate/<pk>',views.updatestudent.as_view()),
    path('deletestudent/<pk>',views.deletestudent.as_view()),
    path('studentreport/<pk>',views.studentreport.as_view()),
    path('studentcard/',views.studentcard),
    path('admisletter/',views.admisletter),
    path('printadmissionletter/', views.PrintAdmissionLetter),
    path('admissionletter/', views.StudentAdmissionLetter),
    # student module close

   #instituteinfo module open
    path('instituteinfo/<id>', views.view_institute_info),
    #instituteinfo module close
    # path('letter/',views.letter),

    #employee module open
    path('allemployee/',views.allemployee,name='home1'),
    path('addemployee/<id>',views.addemployee),
    path('updateemployee/<pk>',views.updateemployee.as_view()),
    path('deleteemployee/<pk>',views.deleteemployee.as_view()),
    path('employeereport/<pk>',views.employeereport.as_view()),
    #employee module close

    # account module open
    path('add_income/<id>',views.addincome),
    path('add_expense/<id>',views.addexpense),
    # path('balance/<pk>',views.account_statement.as_view()),
    path('balance/',views.account_statement,name='home2'),
    path('deleteaccount/<pk>',views.deleteaccount.as_view()),
    # account module close

    #attendence module module
    path('markemplattendence/<id>',views.employee_mark_attendence),
    path('markstudentattendence/',views.student_mark_attendence),
    path('attendencesheet/',views.attendance_sheet),
    path('empattendreport/',views.emp_attend_report),
    path('studattendreport/',views.student_attend_report),
    path('todayattendreport/',views.today_attend_report),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
