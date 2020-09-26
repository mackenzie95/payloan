from django.shortcuts import (render, redirect)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from django.conf import settings
import requests
import random



private_key = settings.PAYSTACK_SECRET_KEY


public_key = settings.PAYSTACK_PUBLIC_KEY


def home(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    return render(request, "home.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST["phone"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard")
        else:
            messages.warning(request, "Invalid login details!!")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/")

def loan(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                password = request.POST["password"]
                conf_pass = request.POST["conf_pass"]
                if password != conf_pass:
                    messages.warning(request, "Passwords do not match!")
                    return render(request, "loan.html")
                first_name = request.session["first_name"]
                last_name = request.session["last_name"]
                email = request.session["email"]
                phone = request.session["phone"]
                loan = request.POST["loan"]
                bvn = request.POST["bvn"]
                bank = request.POST["bank"]
                acc_name = request.POST["acc_name"]
                acc_num = request.POST["acc_num"]
                #id_card = request.POST["id_card"]
                #passport = request.POST["passport"]
            except Exception as e:
                messages.warning(request,"Please fill in the form completely!!")
                return redirect("/apply/stage1")

            try:
                users = User.objects.filter(username=str(phone))
                if len(users) == 0:
                    user = User.objects.create_user(username=str(phone), password=password)
                    user.save()
                else:
                    user = ""
                    messages.warning(request, "Phone number already registered!!")
            finally:
                if user != "":
                    UserProfile = models.UserProfile.objects.create(
                        user = user,
                        first_name = first_name,
                        last_name = last_name,
                        email_address = email,
                        phone = phone,
                        loan_amount = loan,
                        bvn = bvn,
                        bank = bank,
                        account_name = acc_name,
                        account_number = acc_num,
                        )
                    UserProfile.save()
                    request.session.flush()
                    login(request,user)
                    return redirect("/apply/final")
                else:
                    return redirect("/apply/stage1")
    else:
        return redirect("/dashboard")

    return render(request, "loan.html")

 
        
        
def form(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            request.session["first_name"] = request.POST["first_name"]
            request.session["last_name"] = request.POST["last_name"]
            request.session["email"] = request.POST["email"]
            phone = str(request.POST["phone"])
            users = User.objects.filter(username=phone)
            if len(users) != 0:
                messages.warning(request, "Phone already registered!!")
                return redirect("/apply/stage1")

            request.session["phone"] = phone
            return redirect("/apply/stage2")
    else:
        return redirect("/dashboard")
    return render(request, "form.html")


def employ(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            return redirect("/apply/stage3")
    else:
        return redirect("/dashboard")
    return render(request, "employ.html")

@login_required(login_url="/login/")
def final(request):
    user = models.UserProfile.objects.get(user=request.user)
    if user.paid == True:
        return redirect("/dashboard")
    user = models.UserProfile.objects.get(user=request.user)
    email = user.email_address
    phone = user.phone
    first_name = user.first_name
    last_name = user.last_name
    context = {'email':email, 'phone':phone,'first_name':first_name, 'last_name':last_name, "key":public_key}
    return render(request, "card.html",context)



@login_required(login_url="/login/")
def dash(request):
    user = models.UserProfile.objects.get(user=request.user)
    if user.paid != True:
        return redirect("/apply/final")
    user = models.UserProfile.objects.get(user=request.user)
    date = user.app_date
    amount = user.loan_amount
    name = "{0} {1}".format(user.first_name, user.last_name)
    context = {"amount":amount, "date_":date, "name":name}
    return render(request, "dash.html",context)

@login_required(login_url="/login")
def verifyPayment(request):
    try:
        user = models.UserProfile.objects.get(user=request.user)
        ref = request.GET.get("ref")
        headers = {"Authorization": "Bearer {}".format(private_key)}
        resp = requests.get("https://api.paystack.co/transaction/verify/" + ref, headers=headers)
        payment_status = resp.json()["data"]["status"]
        print(payment_status)
        if payment_status == "success":
            user.paid = True
            user.save()
            messages.success(request, "Card verified successfully!!")
            return redirect("/dashboard")
        else:
            raise ValueError("Invalid ref")
    except:
        messages.warning(request, "Card verification not successful!!")
        return redirect("/apply/final")



def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

def tos(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def offices(request):
    return render(request, "offices.html")


