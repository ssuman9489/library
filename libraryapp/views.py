from django.http import HttpResponse
from django.shortcuts import render,redirect
from  .models import *
from django.contrib import messages
from .models import Bookdata
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordResetForm

def home(request):
    return render(request,"home.html")

def main(request):
    return render(request,"main.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login_entry.html")

def login_failure(request):
    return render(request,"login_failure.html")


def logout(request):
    return render(request,"logout.html")

def Book_entry(request):
    return render(request,"Book_entry.html")

def submit(request):
    return render(request,"admin_dashboard.html")

def register(request):
    return render(request,"registration.html")

def forgot_password(request):
    return render(request,"forgot_password.html")

def registration_2(request):
    return render(request,"registration_2.html")

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def student_details(request):
    return render(request, "student_details.html")

def staff_display(request):
    return render(request, "staff_display.html")

def staff_dashboard(request):
    return render(request, "staff_dashboard.html")
 
def student_dashboard(request):
    return render(request, "student_dashboard.html") 

def student_displaybook(request):
    return render(request, "student_displaybook.html")

def book_issue(request):
    return render(request, "book_issue.html")

def select_book(request):
    return render(request, "select_book.html")

def issued_book(request):
    return render(request, "issued_book.html")


def submit(request):
    if(request.method=="POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        T3 = request.POST.get('T3')
        T4 = request.POST.get('T4')
        T5 = request.POST.get('T5')
        T6 = request.POST.get('T6')
        T7 = request.POST.get('T7')
        T8 = request.FILES.get('T8')
        S1 = Bookdata(BookName=T1, Description=T2, Author=T3, Price=T4, Category=T5, Pages=T6, Date_Of_Publish=T7, Photo=T8)
        S1.save()
        return render(request,"admin_dashboard.html")   
    return render(request,"admin_dashboard.html")

def display(request):
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context) 

def student_displaybook(request):
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"student_displaybook.html",context)  

def delete(request,id):
    T1 = Bookdata.objects.get(id=id)
    T1.delete()
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context)


def edit(request,id):
    T1 = Bookdata.objects.get(id=id)
    context = {"T1":T1}
    return render(request,"edit.html",context)

def update(request,id):
    R1=Bookdata.objects.get(id=id)
    if(request.method == "POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        T3 = request.POST.get('T3')
        T4 = request.POST.get('T4')
        T5 = request.POST.get('T5')
        T6 = request.POST.get('T6')
        T7 = request.POST.get('T7')
        T8 = request.FILES.get('T8')
        R1.BookName = T1
        R1.Description = T2
        R1.Author = T3
        R1.Price = T4
        R1.Category  = T5
        R1.Pages = T6
        R1.Date_Of_Publish = T7
        R1.Photo = T8
        R1.save()
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context)

def book(request):
    search_query = request.GET.get('search', '')
    if search_query:
        S1 = Bookdata.objects.filter(BookName__icontains=search_query)
    else:
        S1 = Bookdata.objects.all()
    return render(request, 'student_displaybook.html', {'S1': S1, 'search_query': search_query}) 
    
def book_list(request):
    search_query = request.GET.get('search')
    filter_by = request.GET.get('filter')  
    
    if search_query:
        if filter_by == 'all':  
            books = Bookdata.objects.filter(Q(BookName__icontains=search_query) | 
                                         Q(Description__icontains=search_query) |
                                         Q(Author__icontains=search_query) |
                                         Q(Category__icontains=search_query))
        else:  # Search in the selected field only
            filter_dict = {filter_by + '__icontains': search_query}
            books = Bookdata.objects.filter(**filter_dict)
    else:
        books = Bookdata.objects.all()
    
    context = {
        'S1': books,
        'search_query': search_query
    }
    return render(request, 'display.html', context)
 

def register(request):
    if request.method == 'POST':
        Fullname = request.POST.get('Fullname')
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
               
        # Store personal information in session
        request.session['Fullname'] = Fullname
        request.session['Username'] = Username
        request.session['Email'] = Email
        request.session['Password'] = Password
        return render(request,'registration_2.html')
    return render(request, 'registration.html')

def registration_2(request):
    if request.method == 'POST':
        DOB = request.POST.get('DOB')
        Gender = request.POST.get('Gender')
        category = request.POST.get('category')
        Language = request.POST.get('Language')
        Aadhar = request.POST.get('Aadhar')
        Phone = request.POST.get('Phone')
        Profilepic = request.FILES.get('Profilepic')
        
        Fullname = request.session.get('Fullname')
        Username = request.session.get('Username')
        Email = request.session.get('Email')
        Password = request.session.get('Password')
        D1 = Details(
            Fullname=Fullname,
            Username=Username,
            Email=Email,
            Password=Password,
            DOB=DOB,
            Gender=Gender,
            category=category,
            Language=Language,
            Aadhar=Aadhar,
            Phone=Phone,
            Profilepic=Profilepic
        )
        D1.save() 
        request.session.clear()
        return render(request, 'login_entry.html')   
    return render(request, 'index.html')  
 
def staff_display(request):
    staffs = Details.objects.filter(category='staff')  
    return render(request, 'staff_display.html', {'S1': staffs}) 

def student_details(request):
    students = Details.objects.filter(category='student')  
    return render(request, 'student_details.html', {'S1': students}) 

def login_entry(request):
    return render(request, 'login_entry.html')
    
def login_submit(request):
    if(request.method == "POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        L1 = Details.objects.all().values_list()
        for i in L1:
            if i[2] == T1 and i[4] == T2:
                print("Login Successful")
                if(i[7] == "Admin"):
                    print("Admin Login")
                    return render(request, 'admin_dashboard.html')
            
                elif i[7] == 'staff':
                    print("staff login",i[2],"==",i[3]," ==== ",i[7])
                    return render(request, 'staff_dashboard.html')
                
                elif i[7] == 'student': 
                    print("student login",i[2],"==",i[3]," ==== ",i[7])
                    return render(request, 'student_dashboard.html')   
                else: 
                    messages.error(request, 'Invalid username or password')   
                    return render(request, 'login_entry.html')


def choose(request,id):
    T1 = Bookdata.objects.get(id=id)
    context = {"T1":T1}
    return render(request,"select_book.html",context)

def issue_submit(request):
    if(request.method=="POST"):
        issuedate = request.POST.get('issuedate')
        returndate = request.POST.get('returndate')
        P1 = IssuedBook(issuedate=issuedate,returndate=returndate)
        P1.save()
        return render(request,"student_dashboard.html")   
    return render(request,"select_book.html")

def issue_book(request):
    P1 = IssuedBook.objects.all()
    context = {"P1":P1}
    return render(request,"student_dashboard.html",context) 

def contact_submit(request):
    if(request.method=="POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        S1 = contacts( name=name, email=email, phone=phone, message=message)
        S1.save()
        return render(request,"main.html")   
    return render(request,"contact.html")