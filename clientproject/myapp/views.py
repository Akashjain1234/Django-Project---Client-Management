import datetime
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from myapp.form import SignupForm
from myapp.models import *
from django.contrib import messages



def home_page(request):
    return render (request,"myapp/home.html")

def add_page(request):
    if request.method == 'POST':
        n = request.POST["name"]
        cb = request.POST["createdby"]
        ca = datetime.datetime.now()
        f = Client(name=n,Created_by=cb,Created_at=ca)
        f.save()
        return redirect("/display/")
    return render (request,"myapp/add.html")

def display_page(request):
    data = Client.objects.all()
    context = {"data":data}
    return render (request,"myapp/display.html",context)

def update_page(request,id):
    s1 = Client.objects.get(id=id)
    if request.method == "POST":
        n = request.POST["name"]
        cb = request.POST["createdby"]
        ca = s1.Created_at
        s1.name = n
        s1.Created_by = cb
        s1.Created_at = ca
        s1.save()
        return redirect("/display/")
    context = {"data":s1}
    return render (request,"myapp/update.html",context)

def delete_page(request,id):
    s1 = Client.objects.get(id=id)
    if request.method == "POST":
        s1.delete()
        return redirect("/delsuccess/")
    context = {"data":s1}
    return render (request,"myapp/delete.html",context)

def project_page(request,id):
    user = User.objects.all()
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        n = request.POST.get("name")
        u = request.POST.getlist("user")
        pcb = request.POST["createdby"]
        pca = datetime.datetime.now()
        for i in u:
            p_user = User.objects.get(name=i)
            f = Project(name=n,user=p_user,client=client,procreated_by=pcb,procreated_at=pca)
            f.save()
        return redirect("/displaypro/")
    context = {"user":user,"client":client}
    return render (request,"myapp/addproject.html",context)

def displaypro_page(request):
    data = Project.objects.all()
    context = {"data":data}
    return render (request,"myapp/displaypro.html",context)


def Signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'✔	User Successfully Registred...!')
            uname = request.POST['username']
            a = User(name=uname)
            a.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'myapp/signup.html',context)

def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        user = authenticate(username=uname,password=upass)
        if user == None:
            messages.info(request,'Please Enter Correct Username or Password....! ')
        login(request,user)
        messages.info(request,'Login Successful')
        return redirect('/userinfo/')
    else:
        if request.user.is_authenticated:
            return redirect('/userinfo/')
    return render (request,"myapp/login.html")

def logout_page(request):
    logout(request)
    messages.info(request,'User Successfully Logout')
    return redirect('/')

def clientinfo_page(request,id):
    s1 = Client.objects.get(id=id)
    s2 = Project.objects.filter(client__name__exact=s1.name)
    context = {"data":s1,"pdata":s2}
    return render (request,"myapp/clientinfo.html",context)

def userinfo_page(request):
    uname = Project.objects.filter(user__name__exact=request.user)
    context ={"data":uname}
    return render (request,"myapp/userinfo.html",context)

def delsuccess_page(request):
    return render (request,"myapp/delsuccess.html")

def deletepro_page(request,id):
    s1 = Project.objects.get(id=id)
    if request.method == "POST":
        s1.delete()
        return redirect("/delsuccess/")
    context = {"data":s1}
    return render (request,"myapp/deletepro.html",context)
    
    


