from email.headerregistry import Address
from itertools import product
from os import remove
from sre_constants import CATEGORY_SPACE
from statistics import quantiles
from tabnanny import check
from traceback import print_tb
from turtle import color
from django.http import HttpResponse
from django.shortcuts import render,redirect

#from main.app1.models.color import Color


from .models.product import Product
from .models.category import Category
from .models.color import Color
from .models.chechout import Checkout
from .models.customer import Customer
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.hashers import check_password
# Create your views here.
def shp(request):
    if request.method=='POST':
        product=request.POST['product']
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1 
                else:
                    cart[product]=quantity+1   
            else:
                cart[product]=1          
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        #print(request.session['cart'])
           
        
        return redirect('shp')
    else:
        categories=Category.get_all_categories()

        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
    
        products=None
        categoryid=request.GET.get('category')
        if categoryid:
            products=Product.get_all_products_by_id(categoryid)
        else:
            products=Product.get_all_products()


        
        data={}
        data['products']=products
        data['categories']=categories
        return render(request,'ind.html',data) 
 

def reg(request):
    return render (request,'register.html')

def intro(request):
    error_msg=None
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        customer_det=Customer.get_customer_by_username(username)
        if username=='ashik123' and password=='1234':
            return render (request,'adminpanel.html')
        elif customer_det:
            #print(customer_det)
            request.session['customer']=customer_det.id

            
            #print(request.session.get('customer'))
            if password==customer_det.password:
                
                return redirect('/')
            else:
                error_msg='* invalid username or password'
                return render(request,'intro.html',{'error_msg':error_msg})
                
                
        else:
            error_msg='invalid username or password'
            return render(request,'intro.html',{'error_msg':error_msg})
            
    else:
        
        return render (request,'intro.html')  


def ads(request):
    
    return render(request,'ads.html')


def create(request):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        phone=request.POST['phone']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if Customer.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect ('reg')
                
            elif Customer.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('reg')
            elif len(phone)<10:
                messages.info(request,'phone must be 10 charecters')
                return redirect('reg')    
            else:
                customer= Customer(first_name=first_name,last_name=last_name,username=username,phone=phone,email=email,password=password1)
                customer.save()
                
                return redirect ('intro')
        else:
            messages.info(request,'password not matching')    
            return redirect('reg')  

def logout(request):
    request.session.clear()
    return redirect('intro')


def cart(request):
    try:
        ids=list(request.session.get('cart').keys())
        products=Product.get_all_product_by_id(ids)
        #print (products)
        return render (request,'cart.html',{'products':products})
    except:
        return None

def confirm(request):
    return render(request,'confirm.html')    

def ord(request):
    if request.method=='POST':
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        
        cart=request.session.get('cart')
        products=Product.get_all_product_by_id(cart.keys())
        #print(phone,address,customer,products,cart)
        
        print(customer)
        for product in products:
            
            #print(cart.get(str(product.id)))
            #quantitys=cart.get(str(product.id)) 
            
            checkout=Checkout(product=product,customer=Customer(id=customer),address=address,price=product.price,quantity=cart.get(str(product.id)) , phone=phone)
            checkout.save()

            request.session['cart']={}



        return render(request,'payment.html')
    else:
        return render(request,'sample.html')


def orders(request):
    id=request.session.get('customer')
    
    #cust=(Customer.objects.get(id=id))
    orders=(Checkout.objects.filter(customer_id=id))
    


    

    #idcust=Customer.get_all_customer_by_id(id)
    return render(request,'orders.html',{'orders':orders})
    

def product_admin(request):
    products=Product.objects.all()
    return render(request,'product_admin.html',{'products':products})

def category(request):
    categories=Category.objects.all()
    return render(request,'category.html',{'categories':categories})

def checkout(request):
    checkout=Checkout.objects.all()
    return render(request,'checkout.html',{'checkouts':checkout})

def customer(request):
    customers=Customer.objects.all()
    return render(request,'customer.html',{'customers':customers})    

def add_product(request):
    categories=Category.objects.all()
    colors=Color.objects.all()

    if request.method=='POST':
        category=request.POST['category']
        product=request.POST['product']
        price=request.POST['price']
        description=request.POST['description']
        color=request.POST['color']
        img=request.FILES.get('image')
        
        print(img)
        
        if product=='' or  category=='Choose' or price=='' :
            error_product='invalid format'
            return render(request,'add_product.html',{'error_product':error_product})   

        else:
            product_det= Product(Category_id=category,name=product,price=price,description=description,Color_id=color,img=img)
            product_det.save()
            print('saved')
    
    data={}
    data['categories']=categories
    data['colors']=colors

    return render(request,'add_product.html',data)      

def add_category(request):
    if request.method=='POST':
        name=request.POST['category']
        if name=='':
            error='* empty fiels'
            return render(request,'add_category.html',{'error':error}) 

        else:
            category=Category(name=name)
            category.save()
            return redirect ('category')
    
    return render(request,'add_category.html')       