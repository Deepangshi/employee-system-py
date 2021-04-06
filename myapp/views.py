from django.shortcuts import render
from myapp.models import myapp
from django.contrib import messages
from myapp.forms import empforms


def empdisplay(request):
    result=myapp.objects.all()
    return render(request,"index.html",{"myapp":result})

def empinsert(request):
    if request.method=="POST":
  
            saveemp=myapp()
            saveemp.eid = request.POST.get('eid')
            saveemp.ename = request.POST.get('ename')
            saveemp.eaddress = request.POST.get('eaddress')
            saveemp.egender = request.POST.get('egender')
            saveemp.ephoneno = request.POST.get('ephoneno')
            saveemp.save()
            messages.success(request,"The record "+saveemp.eid+" is saved successfully")
            return render(request,"create.html")
    else:
            return render(request,"create.html")

def empedit(request,empid):
    getemployeedetails=myapp.objects.get(empid-empid)
    return render(request,'edit.html',{"myapp":getemployeedetails})

def empupdate(request,empid):
    empupdate=myapp.objects.get(empid-empid)
    form=empforms(request.POST,instance=empupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The employee record is updated successfully")
        return render(request,"edit.html",{"myapp":empupdate})
def empdel(request,empid):
    delemployee=myapp.objects.get(empid-empid)
    delemployee.delete()
    result=myapp.objects.all()
    return render(request,"index.html",{"myapp":result})




