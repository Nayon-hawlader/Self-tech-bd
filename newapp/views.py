from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Count, Sum, Max
from django.db.models.functions.datetime import ExtractDay
from django.http import request
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect, reverse ,get_object_or_404
from newapp.models import Featured_product, Banner, Deals_of_the_Week, ShopCart,ShopingCartForm,  OderForm, Order, OderProduct, Comment, CommenttForm, FAQ,Featured_productForm,Trend, NewArrival, Blog, Contact, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from UserApp.models import UserProfile
import operator
from datetime import timedelta
from django.db.models import Count, F
from django.utils.timezone import now
from django.db.models.functions import ExtractMonth
from django.views.generic import ListView
from django.db.models import Q
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def handle_not_found(request, exception):
    return render(request, 'not_found.html')

def index(request):
    current_user = request.user
    # blog = ShopCart.objects.all().delete()
    banners =  Banner.objects.all() .order_by('-product_add_date_time') 
    weakly_deals =  Deals_of_the_Week.objects.all() 
    featured_products =  Featured_product.objects.all()
    trend =  Trend.objects.all()
    users=UserProfile.objects.filter(user_id=current_user.id)
    
    best_selers = Featured_product.objects.order_by('amount')[:10]
    best_selers_two = Trend.objects.order_by('amount')[:10]
    review = Comment.objects.all()
    arrival = NewArrival.objects.all()
    
  
    
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity

   
    context = {
        'banners':banners,
        'weakly_deals': weakly_deals,
        'featured_products': featured_products,
        'trend':trend,
        'users':users,
        'arrivals':arrival,
        'cart_product':cart_product,
        'total_product':total_product,
        'total_amount':total_amount,
        'best_selers':best_selers,
        'best_selers_two':best_selers_two,
        'review':review,
        
        
         }
    return render(request, 'index.html', context)

def product_single(request, id):

    featured_products =  Featured_product.objects.all()
    trend =  Trend.objects.all()

    
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0 
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
    single_products = Featured_product.objects.get(id=id)
    comment_show = Comment.objects.filter(p_id=id, status='True')
    color = Featured_productForm()
    users=UserProfile.objects.filter(user_id=current_user.id)
    



    context = {
        'single_products': single_products,       
        'comment_show':comment_show,
        'colors':color,
        'total_product':total_product,
        'total_amount':total_amount,
        'featured_products':featured_products,
        'trend':trend,
        'users':users
        
       
    }
    
    return render(request, 'product_single.html', context)


def Single_product_pro(request, id):
    product_pro = Trend.objects.get(id=id)
    trend_comment = Comment.objects.filter(p_id=id, section='Trend' , status='True')
    
    current_user = request.user
    featured_products =  Featured_product.objects.all()
    trend =  Trend.objects.all()
    users=UserProfile.objects.filter(user_id=current_user.id)


    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
  
   
    context = {
        'product_pro':product_pro,
        'total_product':total_product,
        'total_amount':total_amount,
        'trend_comment':trend_comment,
        'featured_products':featured_products,
        'trend':trend,
        'users':users     
         }
    return render(request, 'single_product_pro.html', context)

    
def Shop(request):
    current_user = request.user
    featured_products =  Featured_product.objects.all()
    trend =  Trend.objects.all()
    userst=UserProfile.objects.filter(user_id=current_user.id)

    featured_count = Featured_product.objects.count()
    trend_count =  Trend.objects.count()

    total_product_count = featured_count + trend_count
  
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity



    page = request.GET.get('page', 1)

  

    paginator = Paginator(featured_products, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)



    context = {
        'featured_products':users, 
        'page_obj':users,  
        'trend':trend,   
        'users':userst,  
        'total_product':total_product,
        'total_amount':total_amount,
        'total_product_count':total_product_count,
        
        
        
         }
    return render(request, 'shop.html', context)


def SearchView(request):  
    current_user = request.user 
    users=UserProfile.objects.filter(user_id=current_user.id)

    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
    featured_products = Featured_product.objects.filter(Q(product_category__icontains=request.GET.get('search')   ) | Q(brand_name__icontains=request.GET['search']))    
        
    context = {
       
        'featured_products':featured_products,
         'total_product':total_product,
        'total_amount':total_amount,
        'users':users
         }
    return render(request, 'searched_result.html', context)


    
def chart_admin(request):
    current_user = request.user
    Tspent = Order.objects.annotate(Total_spent = Count('total'))
    #another variable
    nt=Tspent[0].first_name

    num_post=Order.objects.filter().values('first_name').order_by('user').annotate(sum=Sum('total'))
    n=Order.objects.filter().values('first_name').order_by('user').annotate(sum=Sum('total'))
    nn=Order.objects.filter().values('first_name').order_by('user').annotate(sum=Count('total'))
    nnn=Order.objects.filter().values('first_name').order_by('user').annotate(sum=Max('total'))
    nnnn = Order.objects.filter().values('user').order_by('user').annotate(sum=Sum('total'))
    
  
   
    total_order_by_date=Order.objects.extra({'created':"date(created)"}).values('create_date').annotate(created_count=Count('id'))
    
    best_selers = Featured_product.objects.order_by('amount')[:5]
    
    usercount =  UserProfile.objects.only('id').count() 
 
 
    odrcnt = Order.objects.count()
    td=Order.objects.order_by('-total').annotate(Total_spent = Count('total'))
   
    user_count = UserProfile.objects.count()
 


    Tspednt = Order.objects.filter(total=150).count()
    
    totalsum=Order.objects.aggregate(totalsum=Sum('total'))

    current_user = request.user    
    orders = Order.objects.filter(user_id=current_user.id)
    auths =  Featured_product.objects.order_by('amount')
    # for x in auths:
    #     print (x)
    # for x in sorted(auths, key=operator.attrgetter('amount')):
    #     print (x)
    best_selers = Featured_product.objects.order_by('amount')[:5]
    # for x in myauths:
    #     print (x)
    author_count = Featured_product.objects.count()
    # cut_off_score = Featured_product.objects.order_by('-amount').values_list('amount')[min(3, author_count)]
    #top_authors = Featured_product.objects.filter(score__gte=cut_off_score).order_by('amount')    
    m=Order.objects.all()
    # n= m.values('first_name').annotate(Count('id'))
    # n= m.values('total').annotate(Count('id'))
    context = {
        'Tspent':Tspent,
        'num_post':num_post,
        'Tspednt':Tspednt,
        'n':n,
        'td':td,
        'nt':nt,
        'author_count':author_count,
        'user_count':user_count,
        'nn':nn,
        'nnn':nnn,
        'nm':nnnn,
        'm':m,
        'odrcnt':odrcnt,
        'total_order_by_date':total_order_by_date,
        'usercount':usercount,
        'best_selers':best_selers
        
    }
    
    return render(request, 'chart_admin.html', context)
  




@login_required(login_url='/user/login')
def Add_to_Shoping_cart(request, id):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')

    # get single or more column value from model
    # active_emps_first_name = Employees.objects.filter(active=True).values_list('first_name',flat=True)
    # ployees.objects.filter().only('eng_name')
    # mycart  = ShopCart.objects.values_list('p_id','section')
    
    shopcart=ShopCart.objects.filter(user=current_user,p_id=id, section='Featured').exists()
    cart,created = Featured_product.objects.get_or_create(id=id)
    if shopcart is True:      
        order,created = ShopCart.objects.get_or_create(p_id=id,current_price=cart.current_price, section='Featured')
        order.quantity += 1
        order.save()
        messages.success(request, 'Your  product has been updated')
    else:    
        order = ShopCart()
        order.user_id = current_user.id
        order.p_id = id
        order.brand_name = cart.brand_name
        order.current_price = cart.current_price
        order.quantity = 1
        order.section = 'Featured'
        order.product_photo_main = cart.product_photo_main
        order.save()    
        messages.success(request, 'Your  product has been added')
    return HttpResponseRedirect(url)


@login_required(login_url='/user/login')
def Add_to_Shoping_cart_trend(request, id):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')
    shopcart=ShopCart.objects.filter(user=current_user,p_id=id, section='Trend').exists()
    cart,created = Trend.objects.get_or_create(id=id)
    form = ShopingCartForm(request.POST)    
    if form.is_valid():
        if shopcart is True:                    
            order,created = ShopCart.objects.get_or_create(p_id=id,current_price=cart.current_price, section='Trend')
            order.quantity += form.cleaned_data['quantity']
            order.save()
            messages.success(request, 'Your  product has been updated')
        else:
            order = ShopCart()
            order.user_id = current_user.id
            order.p_id = id
            order.brand_name = cart.brand_name
            order.current_price = cart.current_price
            order.quantity = form.cleaned_data['quantity']
            order.section = 'Trend'
            order.product_photo_main = cart.product_photo_main
            order.save() 
            messages.success(request, 'Your  product has been updated')
    else: 
        order = ShopCart()
        order.user_id = current_user.id
        order.p_id = id
        order.brand_name = cart.brand_name
        order.current_price = cart.current_price
        order.quantity = 1
        order.section = 'Trend'
        order.product_photo_main = cart.product_photo_main
        order.save()    
        messages.success(request, 'Your  product has been added')
    return HttpResponseRedirect(url)

@login_required(login_url='/user/login')
def Add_to_Shoping_cart_form(request, id):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')
    shopcart=ShopCart.objects.filter(user=current_user,p_id=id, section='Featured').exists()
    cart,created = Featured_product.objects.get_or_create(id=id)    
    form = ShopingCartForm(request.POST)
    if form.is_valid():
            if shopcart is True:
                order,created = ShopCart.objects.get_or_create(user_id=current_user.id,p_id=id,current_price=cart.current_price, section='Featured')
                order.quantity += form.cleaned_data['quantity']
                order.color = form.cleaned_data['color']
                order.save()
                messages.success(request, 'Your  product has been updated')

            else:
                order = ShopCart()
                order.user_id = current_user.id
                order.p_id = id
                order.brand_name = cart.brand_name
                order.current_price = cart.current_price
                order.quantity = form.cleaned_data['quantity']
                order.color = form.cleaned_data['color']
                order.section = 'Featured'
                order.product_photo_main = cart.product_photo_main
                order.save()    
                messages.success(request, 'Your  product has been added')                
    return HttpResponseRedirect(url)
  
def cart_details(request):
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
    category = Featured_product.objects.all()
    users=UserProfile.objects.filter(user_id=current_user.id)

    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user)


    sum_total= 0
    for Tsum in cart_product:
        sum_total += Tsum.current_price*Tsum.quantity
    context = {
        'category': category,
        'cart_product':cart_product,
        'sum_total':sum_total,
        'total_product':total_product,
        'total_amount':total_amount,
        'users':users

    }
    return render(request, 'cart.html', context)

def cart_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user=request.user
    cart_product=ShopCart.objects.filter(id=id, user_id=current_user.id)
    cart_product.delete()
    messages.success(request, 'Your Product  has been delete')
    return HttpResponseRedirect(url)




@login_required(login_url='/user/login')
def OrderCart(request):

    current_user = request.user
    shoping_cart = ShopCart.objects.filter(user_id=current_user.id)
    users=UserProfile.objects.filter(user_id=current_user.id)
    totalamount = 0
    for rs in shoping_cart:
        totalamount += rs.quantity*rs.current_price

    total_product=0    
    for quantities in shoping_cart:
        total_product =total_product+quantities.quantity


    if request.method == "POST":
        form = OderForm(request.POST, request.FILES)
        if form.is_valid():
            dat = Order()
            # get product quantity from form
            dat.first_name = form.cleaned_data['first_name']
            dat.last_name = form.cleaned_data['last_name']
            dat.address = form.cleaned_data['address']
            dat.city = form.cleaned_data['city']
            dat.phone = form.cleaned_data['phone']
            dat.country = form.cleaned_data['country']
            dat.user_id = current_user.id                     
            if 'gift' in request.POST:
                dat.total = totalamount+70
            else:
                dat.total = totalamount+50
            dat.gift = form.cleaned_data['gift']       
            dat.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random cod
            dat.code = ordercode
            dat.save()

            # moving data shopcart to product cart
            for rs in shoping_cart:
                data = OderProduct()
                data.order_id = dat.id
                data.p_id = rs.p_id
                data.user = current_user
                data.user_address = form.cleaned_data['address']
                data.phone = form.cleaned_data['phone']
                data.email = form.cleaned_data['email']
                data.quantity = rs.quantity
                data.color = rs.color
                data.price = rs.current_price  
                data.brand_name = rs.brand_name 
                data.section = rs.section 
                data.product_photo_main = rs.product_photo_main 
                if 'gift' in request.POST:
                    data.total_amount = totalamount+70
                else:
                    data.total_amount = totalamount+50           
                data.amount = rs.amount()
                data.save()
                
                product = Featured_product.objects.get(id=rs.p_id)
                product.amount -= rs.quantity
                product.save()

            # Now remove all order data from the shoping cart
            ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your oder has been completed')
            category = Featured_product.objects.all()
           
            context = {
                # 'category':category,
                'ordercode': ordercode,
                'category': category,
                'total_amount': totalamount,
                'total_product':total_product,
                'users':users
                
            }

            return render(request, 'oder_completed.html', context)
        else:
            messages.warning(request, form.errors)
          #  return HttpResponseRedirect("/order/oder_cart")
    form = OderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    
    sum_total= 0
    for Tsum in shoping_cart:
        sum_total += Tsum.current_price*Tsum.quantity
    
    total_quantity = 0
    total_amount = 50
    for p in shoping_cart:
        total_amount += p.current_price*p.quantity
        total_quantity += p.quantity
    
    category = Featured_product.objects.all()
    
    gift=float(20)
    context = {
       
        'shoping_cart': shoping_cart,
        'totalamount': totalamount,                
        'profile': profile,
        'form': form,
        'category': category,        
        'total_amount': total_amount,
        'total_product':total_product,        
        'gift':gift,
        'sum_total':sum_total,
        'users':users
    }
    return render(request, 'order_form.html', context)



  
 




def comment_add(request, id):    
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommenttForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.subject = pos.cleaned_data['subject']
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            data.p_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.brand_name=pos.cleaned_data['brand_name']
            data.section="Featured"
            data.save()
            messages.success(request, 'Your comment has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def comment_trend(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommenttForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.subject = pos.cleaned_data['subject']
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_trend_id = id
            data.p_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.brand_name=pos.cleaned_data['brand_name']
            data.section="Trend"
            data.save()
            messages.success(request, 'Your comment has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def Blog_Post(request):
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    users=UserProfile.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity

   

    blog = Blog.objects.all()
    

    
    # delete cmd
    # blog = Blog.objects.all()[0].delete()

    context = {
        'blog': blog,  
        'total_product':total_product,
        'total_amount':total_amount,
        'users':users
        
        
        

    }
    return render(request, 'blog.html', context)
def Blog_single(request, id):
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    users=UserProfile.objects.filter(user_id=current_user.id)

    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity


    blog = Blog.objects.get(id=id)
    
    items = list(Blog.objects.all())
    bloglist = random.sample(items, 3)


    context = {
        'blog': blog,    
        'bloglist':bloglist,
        'total_product':total_product,
        'total_amount':total_amount,
        'users':users
    }
    return render(request, 'blog_single.html', context)


def Cashmemo(request):
    
    user = UserProfile.objects.all()
    cashmemo_two = OderProduct.objects.all()

    
    context = {
     'user':user,
     'cashmemo_two':cashmemo_two

    }
    return render(request, 'cashmemo.html', context)

def Faq_details(request):
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity


    category = Featured_product.objects.all()    
    faq = FAQ.objects.filter(status=True).order_by('created_at')

    context = {
        'category': category,     
        'faq': faq,
        'total_product':total_product,
        'total_amount':total_amount,

    }
    return render(request, 'faq.html', context)

def Contact(request):
    current_user = request.user
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    users=UserProfile.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
 

    form = ContactForm(request.POST) 
    if request.method == "POST":        
        if form.is_valid():
            form.save()
            

   
    context = {
        'form': form,
        'total_product':total_product,
        'total_amount':total_amount,
        'users':users
     
        }
    return render(request, 'contact.html', context)