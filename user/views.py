from django.shortcuts import render,redirect
from .models import RegisterModel,ProductModel,BidTableModel
from django.contrib import messages
from django.db.models import Q

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

    return None


def user_logout(request):
    del request.session["user_username"]
    return redirect('index')


def save_product(request):
    pno = request.POST["p1"]
    pname = request.POST["p2"]
    bidding_price = request.POST["p3"]
    pinfo = request.POST["p4"]
    pimage = request.FILES["p5"]
    pstatus = "bidding"
    puser = request.session["user_idno"]

    ProductModel(pid=pno,name=pname,bprice=bidding_price,info=pinfo,image=pimage,status=pstatus,user_id=puser).save()

    return sellproduct(request)
    # data = ProductModel.objects.filter(user_id=request.session["user_idno"])
    # return render(request, "users_template/sell_product.html", {"data": data})


def sellproduct(request):
    data = ProductModel.objects.filter(user_id=request.session["user_idno"])
    return render(request,"users_template/sell_product.html",{"data":data})



def bid_product(request):

    qs = ProductModel.objects.filter(status="bidding") & ProductModel.objects.filter(~Q(user_id=request.session["user_idno"]))

    return render(request,"users_template/bid_products.html",{"data":qs})


def bid_amount(request):
    amount= request.POST["p1"]
    pid = request.POST["p2"]
    uid = request.POST["p3"]

    BidTableModel(amount=amount,product_id_id=pid,user_id_id=uid).save()

    return bid_product(request)


def bidDetails(request):
    pid = request.GET.get("pid")
    qs = BidTableModel.objects.filter(product_id_id=pid)
    d = {"pid":pid}
    return render(request,"users_template/biddetails.html",{"data":qs,"pno":d})


def bDetails(request):
    pid = request.GET.get("pid")
    qs = BidTableModel.objects.filter(product_id_id=pid)
    d = {"pid": pid}
    return render(request, "users_template/bdetails.html", {"data": qs, "pno": d})
