from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.db.models import Q
import random
# Create your views here.

# CONTACT PAGE OF COMPANY
def contact(request):
    return render(request,'pages/contact.html')
    # return HttpResponse("Contact page")

# SIGNUP PAGE FOR COMPANY
def signup(request):
    if request.method=='POST':
        nm = request.POST['name']
        em = request.POST['email']
        num = request.POST['number']
        pas = request.POST['password']
        
        try:
            var = CompanyDetail.objects.get(c_email = em)
            return HttpResponse("<h1><a href=""> Email Id Already Registered... </a></h1>")    
        except:
            obj = CompanyDetail()
            obj.c_name = nm
            obj.c_email = em
            obj.c_cno = num
            obj.c_pass = pas
            obj.save()
            return redirect('login')
    return render(request,'pages/signup.html')

# ABOUT PAGE OF COMPANY
def about(request):
    return render(request,'pages/about.html')

# HOME PAGE OF COMPANY
def home(request):
    prods = CompanyProduct.objects.all()
    q=request.GET.get('search')
    if q:
        pr=CompanyProduct.objects.filter(Q(prod_nm__icontains=q)| Q(prod_price__icontains=q))
        return render(request,'pages/home.html',{'pr':pr})
    else:
        return render(request,'pages/home.html',{'prod':prods})

# SIGNUP DUMMY
def datapost(request):
    if request.method=='POST':
        model = Product()
        model.name = request.POST['username']
        model.email = request.POST['email']
        model.save()
    return render(request,'pages/datapost.html')

# PARTICULAR PRODUCT VIEW dummy
def productview(request,abc):
    v=Pro.objects.get(id=abc)
    return render(request,'pages/productview.html',{'v':v})

# ALL PRODUCT VIEW dummy
def proall(request):
    if 'xyz' in request.session.keys():
        l = Pro.objects.all()
        return render(request,'pages/proall.html',{'l':l})
    else:
        return redirect('login')

# LOGIN PAGE FOR COMPANY
def loginview(request):
    if request.method=='POST':
        try:
            m=CompanyDetail.objects.get(c_email=request.POST['email'])
            if m.c_pass == request.POST['pass']:
                request.session['xyz']=m.id
                return redirect('profile')
            else :
                return HttpResponse('<h1>Invalid Password</h1>')
        except:
            return HttpResponse('<h1>Wrong Email</h1>')
    return render(request,'pages/login.html')


# SEARCH BAR LOGIC for all product at home page 
def searchview(request):
    prods = CompanyProduct.objects.all()
    q=request.GET.get('search')
    if q:
        pr=CompanyProduct.objects.filter(Q(prod_nm__icontains=q)| Q(prod_price__icontains=q))
        return render(request,'pages/home.html',{'pr':pr})
    else:
        return render(request,'pages/home.html',{'prod':prods})

# DELETE PRODUCT FOR VENDOR dummy
def productdelete(request,abc):
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('proall')

# LOGOUT LOGIC *this is vendor logout*
def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
    return redirect('login')
# dummy
def productadd(request):
    if request.method=='POST':
        model = Pro()
        model.name = request.POST['name']
        model.description = request.POST['description']
        model.price = request.POST['price']
        model.image = request.FILES.get('image')
        model.review = request.POST['review']
        model.save()
    return render(request,'pages/productadd.html')

# Update Profile Function
# Landing page of vendor
def profile_manage(request):
    if 'xyz' in request.session.keys():
        comp = CompanyDetail.objects.get(id = int(request.session['xyz']))
        if request.POST:
            comp.c_name = request.POST['nm1']
            comp.c_email = request.POST['em1']
            comp.c_cno = request.POST['con1']
            comp.c_add = request.POST['add1']
            comp.c_pass = request.POST['pass1']
            img1 = request.FILES.get('img1')
            
            print(img1)
            if img1 != None:
                comp.profile = img1

            comp.save()
        return render(request,'vendor/profile_manage.html',{'USERS':comp})
    else:
        return redirect('login')

# ---- VENDOR ---- DASHBOARD
def addCustomer(request):
    if 'xyz' in request.session.keys():
        comp = CompanyDetail.objects.get(id = int(request.session['xyz']))
        if request.method=='POST':
            nm = request.POST['nm1']
            em = request.POST['em1']
            con = request.POST['con1']
                
            obj = CompanyCustomer()
            obj.comp = comp
            obj.cust_nm = nm
            obj.cust_em = em
            obj.cust_con = con
            
            # Password Create---------
            CHAR = 'qwertyuiopasdfghjklzxcvbnm'
            otp = ""
            for i in range(8):
                otp += str(random.choice(CHAR))        
            obj.cust_pass = otp
            obj.save()
            return redirect('viewC')    
        return render(request,'vendor/addCustomer.html',{'USERS':comp})
    else:
        return redirect('login')

def viewCustomer(request):
    if 'xyz' in request.session.keys():
        comp_user = CompanyDetail.objects.get(id = int(request.session['xyz']))
        custs = CompanyCustomer.objects.filter(comp=comp_user)
        return render(request,'vendor/viewCustomer.html',{'USERS':comp_user,'cust':custs})
    else:
        return redirect('login')
# delete customer which is inside viewCustomer
def DeleteCustomer(request,abc):
    if 'xyz' in request.session.keys():
        c=CompanyCustomer.objects.get(id=abc)
        c.delete()
        return redirect('viewC')
    else:
        return redirect('login')

def addProduct(request):
    if 'xyz' in request.session.keys():
        p=CompanyProduct()
        comp=CompanyDetail.objects.get(id=request.session['xyz'])
        if request.method=='POST':
            # if you will use square bracket in above get method instead of parentheses you will type error
            p.comp=comp
            p.prod_img = request.FILES.get('img1')
            p.prod_nm=request.POST['nm1']
            p.prod_price=request.POST['pr1']
            p.prod_qty=request.POST['qty1']
            p.save()
            return redirect('viewP')
        return render(request,'vendor/addProduct.html',{'USERS':comp})
    else:
        return redirect('login')
    
def DeleteProduct(request,abc):
    if 'xyz' in request.session.keys():
        prod = CompanyProduct.objects.get(id = abc)
        prod.delete()
        return redirect('viewP')
    else:
        return redirect('login')
    
def UpdateProduct(request,abc):
    if 'xyz' in request.session.keys():
        comp = CompanyDetail.objects.get(id = int(request.session['xyz']))
        prod = CompanyProduct.objects.get(id = abc)
        if request.POST:
            nm = request.POST['nm1']
            pr = request.POST['pr1']
            qty = request.POST['qty1']
            img = request.FILES.get('img1')
            
            prod.comp = comp
            prod.prod_nm = nm
            prod.prod_price = pr
            prod.prod_qty = qty
            if img != None:
                prod.prod_img = img
            prod.save()
            return redirect('viewP')
        return render(request,'vendor/updateProduct.html',{'USERS':comp,'prod':prod})
    else:
        return redirect('login')

def viewProduct(request):
    if 'xyz' in request.session.keys():
        comp = CompanyDetail.objects.get(id=int(request.session['xyz']))
        prods= CompanyProduct.objects.filter(comp=comp)
        q= request.GET.get('searchC')
        if q:
            prods=prods.filter(Q(prod_nm__icontains=q)| Q(prod_price__icontains=q))
        return render(request,'vendor/viewProduct.html',{'USERS':comp,'pr':prods})
    else:
        return redirect('login')