from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from ExpenseTracker.models import Exp
from ExpenseTracker.forms import stform
import random
#from .models import ExpenseInfo
#from ExpenseTracker.models import ExpenseInfo
#from ExpenseTracker.models import AccountInfo
#from django.contrib.auth import login as auth_login
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np


def login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            authenticate(username=uname,password=upass)
            if User is not None:

                results=Exp.objects.filter(owner=request.user)
                return render(request,'dashboard1.html',{"Exp":results})
                #return HttpResponseRedirect('/dashboard1/.html')
    else:
        fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    return render(request,'login.html',{'form':fm})    

def register(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Suceessfully')
            fm.save()
            username = fm.cleaned_data.get('username')
            password1 = fm.cleaned_data.get('password1')
            password2 = fm.cleaned_data.get('password2')
            user = authenticate(username=username,password=password1)
            messages.success(request,'Registeration sucessfull')
            print("Created sucessfully")
            return HttpResponseRedirect('/register/')
            #return render(request,'login.html',{'form':fm})  
    else:
        fm = UserCreationForm()
        return render(request,'register.html',{'form':fm})
    return render(request,'register.html',{'form':fm})


'''
def  insert(request):

    if request.method=="POST":
        if request.POST.get('des') and request.POST.get('amt') and request.POST.get('date') and request.POST.get('pay'):
            savest=Exp(owner=request.user)
            #savest.owner=request.POST.get('owner')
            savest.des=request.POST.get('des')
            savest.amt=request.POST.get('amt')
            savest.date=request.POST.get('date')
            savest.pay=request.POST.get('pay')
            savest.save()
            messages.success(request,'The record saved')
            return render(request,'create.html')
        else:
            return render(request,'create.html')
    return render(request,'create.html')        


'''
def insert(request,user_id):
    display_course=User.objects.get(id=user_id)
    print(display_course)
    if request.method=="GET":
        return render(request,'create.html',{'display':display_course})
    elif request.method=="POST":
        try:
            des=request.POST['des']
            amt=request.POST['amt']
            date=request.POST['date']
            pay=request.POST['pay']
            Exp(des=des,amt=amt,date=date,pay=pay,owner_id=user_id).save()
            messages.success(request,'Record saved suceesfully')
            return render(request,'create.html',{'display':display_course})
        except Exception as e:
            messages.successs(request,'Failed')          
    return render(request,'create.html',{'display':display_course})









def create(request):
    return render(request,'create.html')

def index(request):
    return render(request,'index.html')
    

def show_expense(request,user_id):#Foreign key problem filter user
    if request.user.is_authenticated:
        point = User.objects.get(id=user_id)
        results=Exp.objects.filter(owner=point)
        print(request.user.id)
        return render(request,'index.html',{"Exp":results})

def dash(request,user_id):#Foreign ley problem filter user
    if request.user.is_authenticated:
        point = User.objects.get(id=user_id)
        print(point)
        results = Exp.objects.filter(owner=point)
    #results=Exp.objects.filter(owner=request.user)
        return render(request,'dashboard1.html',{"Exp":results})

    
def edit(request,id):
    getexpense=Exp.objects.get(id=id)
    return render(request,'edit.html',{"Exp":getexpense})

def stupdate(request,id):
    stupdate=Exp.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,'Expense updated successfully')
        return render(request,'edit.html',{"Exp":stupdate})
    #else:
        #return render(request,'edit.html',{"Exp":stupdate})

def stdel(request,id):
    delstudent=Exp.objects.get(id=id)
    delstudent.delete()
    owner = User.objects.get(id=request.user.id )
    results = Exp.objects.filter(owner=owner)
    #results=Exp.objects.filter(owner=request.user)
    return render(request,'dashboard1.html',{"Exp":results})

def logout(request):
     return HttpResponseRedirect('/login/')




def piechart(request,user_id):
    if request.user.is_authenticated:
        labels = []
        data = []
        point = User.objects.get(id=user_id)
        queryset = Exp.objects.filter(owner=point)
        for city in queryset:
            labels.append(city.des)
            data.append(city.amt)
        explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(data, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('static\css\images.png',dpi=100)
        return render(request,'pie.html')  
   # return render(request,'pie.html',{'labels':labels,'data':data})    
