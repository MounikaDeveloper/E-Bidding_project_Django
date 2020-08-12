from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from user.models import RegisterModel
from badmin.smsprocess import sendSMS


def check_admin(request):
    username = request.POST["a1"]
    password = request.POST["a2"]
    if username == "admin" and password == "admin":
        return redirect("admin_home")
    else:
        messages.error(request,"Invalid Details")
        return redirect("admin_login")


def pendingReg(request):
    qs = RegisterModel.objects.filter(status="pending")
    return render(request,"badmin_template/pending_reg.html",{"data":qs})

def approvedReg(request):
    qs = RegisterModel.objects.filter(status="approved")
    return render(request,"badmin_template/approved_reg.html",{"data":qs})

def declineReg(request):
    qs = RegisterModel.objects.filter(status="decline")
    return render(request,"badmin_template/decline_reg.html",{"data":qs})


def approve(request):
    idno = request.POST["a1"]
    qs = RegisterModel.objects.filter(id=idno)
    name = ""
    cno = ""
    for x in qs:
        name = x.name
        cno = x.contact
    qs.update(status="approved")

    mess = "Hello Mr/Miss : "+name+". Your Registration is Approved"
    x = sendSMS(str(cno),mess)
    print(x)
    return redirect('approved_reg')


def decline(request):
    idno = request.POST["a2"]
    qs = RegisterModel.objects.filter(id=idno)
    name = ""
    cno = ""
    for x in qs:
        name = x.name
        cno = x.contact
    qs.update(status="decline")

    mess = "Hello Mr/Miss : " + name + ". Your Registration is Declined"
    x = sendSMS(str(cno), mess)
    print(x)
    return redirect('decline_reg')


def logoutAdmin(request):
    return redirect('index')