from django.db import models
from datetime import date

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

class Product(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(default='')
    
    def __str__(self):
        return self.name

class Signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    password=models.CharField(max_length=20)
    

    def __str__(self):
        return str(self.mobile_no)

class Pro(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pro')
    review = models.TextField()
    
class subadmin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    contact=models.IntegerField(default=0)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.PositiveIntegerField()
    password=models.CharField(max_length=10)

# Create your models here.

# sign up for company
class CompanyDetail(models.Model):
    c_name = models.CharField(default="",max_length=200)
    c_email = models.EmailField(default="",max_length=200)
    c_pass = models.CharField(default="",max_length=200)
    c_cno = models.CharField(default="",max_length=50)
    c_add = models.TextField(default="")
    join_date = models.DateField(auto_now=True,blank=True,null=True)
    profile = models.ImageField(upload_to="Com_Prof/",max_length=300,default="",blank=True,null=True) 
    def __str__(self):
        return str(self.c_name)

# sign up for customers
class CompanyCustomer(models.Model):
    comp = models.ForeignKey('CompanyDetail',on_delete=models.CASCADE,blank=True, null=True)
    cust_nm = models.CharField(default="",max_length=200)
    cust_em = models.EmailField(default="",max_length=200)
    cust_con = models.CharField(default="",max_length=50)
    cust_add1 = models.TextField(default="")
    cust_add2 = models.TextField(default="")
    cust_pass = models.CharField(default="",max_length=200)
    cust_regi_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    cust_profile = models.ImageField(upload_to="Cust_Pic/",max_length=300,default="",blank=True,null=True)
    def __str__(self):
        return str(self.cust_nm) 

# products for company
class CompanyProduct(models.Model):
    comp = models.ForeignKey('CompanyDetail',on_delete=models.CASCADE,blank=True, null=True)
    prod_nm = models.CharField(default="",max_length=200)
    prod_price = models.PositiveIntegerField(default=0)
    prod_qty = models.PositiveIntegerField(default=0)
    prod_img = models.ImageField(upload_to="ProductPic/",max_length=300,default="",blank=True,null=True) 
    def __str__(self):
        return str(self.prod_nm)