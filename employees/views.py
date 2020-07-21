from django.shortcuts import render,redirect
from django.http import HttpResponse

from employees.models import *

# Create your views here.
def signup(request):

    data={
        'regval':'true',
        'logval':'false',
        'rval':'active',
        'lval':''
    }

    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        eid = request.POST['eid']
        fpassword = request.POST['fpassword']
        spassword = request.POST['spassword']
        gender = request.POST['gender']
        email = request.POST['email']
        age = request.POST['age']
        salary = request.POST['salary']
        phoneno = request.POST['phoneno']
        department = request.POST['department'] 

        #print(fname,lname,eid,fpassword,spassword, gender ,email ,age, salary,  phoneno , department)
       
        EmployeeRegister.objects.create(Emp_Firstname=fname,Emp_Lastname=lname,Emp_Age=age,Emp_Id=eid,Emp_Gender=gender,Emp_Email=email,Emp_Password=fpassword,Emp_Salary=salary,Emp_Department=department,Emp_phoneno=phoneno)
        data={
        'regval':'false',
        'logval':'true',
        'rval':'',
        'lval':'active'
        }
        render(request,'employees/signup.html',data)
    
    return render(request,'employees/signup.html',data)


def login(request):
    data={
        'regval':'false',
        'logval':'true',
        'rval':'',
        'lval':'active'
    }
    if request.method=="POST":
        fname = request.POST['l_fname']
        lname = request.POST['l_lname']
        email = request.POST['l_email']
        password = request.POST['l_password']

        d=EmployeeRegister.objects.filter(Emp_Firstname=fname,Emp_Lastname=lname,Emp_Password=password,Emp_Email=email)
        
        if len(d)!=0:

            
            data['username']=fname+" "+lname
            data['empid']=d [0].Emp_Id
            return render(request,'employees/mainpage.html',data) 

        else:
            data['message']="you have entered invalid credentials try again"
            
            return render(request,'employees/signup.html',data)
            


    return render(request,'employees/signup.html',data)
    


def updatedetails(request):
    data={
        'regval':'true',
        'logval':'false',
        'rval':'active',
        'lval':''
    }
    if request.method=='POST':
        eid=request.POST['empid']

        data['empid']=eid
        return render(request,'employees/updatedetails.html',data)



    return render(request,'employees/signup.html',data)



def mainpage(request):
    data={
        'regval':'true',
        'logval':'false',
        'rval':'active',
        'lval':''
    }


    return render(request,'employees/signup.html',data)



def showdata(request):

    data={
        'empdata' : EmployeeRegister.objects.all()
    }

    return render(request,'employees/showdata.html',data)



def edit(request,epid):
  

    obj=EmployeeRegister.objects.get(id=epid)
    
    data={
        'obj':obj
    }
    if request.method=='POST':
        print("thid is post method")
        d=EmployeeRegister.objects.get(id=epid)
        d.delete()
        fname = request.POST['fname']
        lname = request.POST['lname']
        eid = request.POST['eid']
        fpassword = request.POST['fpassword']
        spassword = request.POST['spassword']
        gender = request.POST['gender']
        email = request.POST['email']
        age = request.POST['age']
        salary = request.POST['salary']
        phoneno = request.POST['phoneno']
        department = request.POST['department'] 

        EmployeeRegister.objects.create(Emp_Firstname=fname,Emp_Lastname=lname,Emp_Age=age,Emp_Id=eid,Emp_Gender=gender,Emp_Email=email,Emp_Password=fpassword,Emp_Salary=salary,Emp_Department=department,Emp_phoneno=phoneno)

        data={
        'empdata' : EmployeeRegister.objects.all()
        }

        return render(request,'employees/showdata.html',data)

        
    print("this is get method")
    return render(request,'employees/edit.html',data)




def delete(request,epid):

    d=EmployeeRegister.objects.get(id=epid)
    d.delete()

    return redirect('../../showdata')

    