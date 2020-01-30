from django.shortcuts import render,redirect
from .models import RegisterModel, ProductModel1
from django.contrib import messages

def registerUser(request):
    name = request.POST["s1"]
    contact = request.POST["s2"]
    email = request.POST["s3"]
    password = request.POST["s4"]
    status = "pending"
    RegisterModel(name=name,contact=contact,email=email,password=password,status=status).save()
    messages.success(request,"Registration Need to Approve By Admin")
    return redirect("buyer_seller")


def userlogin(request):
    cno = request.POST["b1"]
    password = request.POST["b2"]
    try:
        res = RegisterModel.objects.get(contact=cno,password=password)

        if res.status == "approved":
            request.session["user_username"] = res.name
            request.session["user_idno"] = res.id
            return render(request,"users_template/user_home.html")
        elif res.status == "pending":
            messages.error(request, "Your Registration in Pending")
            return redirect("buyer_seller")
        else:
            messages.error(request, "Your Registration in Declined")
            return redirect("buyer_seller")

    except RegisterModel.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("buyer_seller")




def user_logout(request):
    del request.session["user_username"]
    return redirect('index')


def productsave(request):
    pno=request.POST["pno"]
    pname=request.POST["pname"]
    bprice=request.POST["bprice"]
    info=request.POST["info"]
    image=request.FILES["image"]
    sellerinfo=request.session["user_idno"]
    ProductModel1(pno=pno,pname=pname,bidprice=bprice,information=info,image=image,status="Inactive",sellerinfo_id=sellerinfo).save()
    return sellproduct(request)


def sellproduct(request):
    x=ProductModel1.objects.all()
    return render(request,"users_template/sell_product.html",{"data":x})


def removeproduct(request):
    x=request.GET.get("x")
    ProductModel1.objects.get(pno=x).delete()
    return redirect("user_home")