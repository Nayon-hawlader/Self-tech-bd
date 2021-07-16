from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from UserApp.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from UserApp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.forms import PasswordChangeForm
from UserApp.models import UserProfile
from newapp.models import Featured_product, Banner, Deals_of_the_Week, Order, ShopCart, Comment

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Your username or password is invalid')
    featured_product=Featured_product.objects.all()

    context={
            'featured_product':featured_product
        }
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')



def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "user_img/user.svg"
            data.save()

            return redirect('index')
        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    featured_product = Featured_product.objects.all()
   
    context = {'featured_product': featured_product,              
               'form': form}
    return render(request, 'user_register.html', context)


    



def userprofile(request):
    featured_product = Featured_product.objects.all()
 
    current_user = request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
  
        
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
    context = {'featured_product': featured_product,
               
               'profile': profile,
               'total_amount':total_amount,               
               'total_product':total_product,
               
               }
    return render(request, 'user_profile.html', context) 



def track_order(request):
    featured_product = Featured_product.objects.all()
    current_user = request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    order = Order.objects.filter(user_id=current_user.id)  
  
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity


    context = {'featured_product': featured_product,
               
               'profile': profile,
               'order': order,
               'total_amount':total_amount,               
               'total_product':total_product,      
               
               }
    return render(request, 'track_order.html', context) 



@login_required(login_url='/user/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('userprofile')
    else:
       # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = ProfileUpdateForm(instance=request.user)
        featured_product = Featured_product.objects.all()

        current_user = request.user
        cart_product= ShopCart.objects.filter(user_id=current_user.id)
        total_amount=0
        for product in cart_product:
            total_amount+=product.current_price*product.quantity
        total_product=0    
        for quantities in cart_product:
            total_product =total_product+quantities.quantity
    
       
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'featured_product': featured_product,
            'total_amount':total_amount,               
            'total_product':total_product,
           
        }
        return render(request, 'userupdate.html', context)




@login_required(login_url='/user/login')  # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('userprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('user_password')
    else:
        featured_product = Featured_product.objects.all()
        
        form = PasswordChangeForm(request.user)
        return render(request, 'userpasswordupdate.html', {'form': form,
                                                           'featured_product': featured_product,
                                                           

                                                           })
@login_required(login_url='/user/login')
def usercomment(request):
    category = Featured_product.objects.all()
    
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)

    
  
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for product in cart_product:
        total_amount+=product.current_price*product.quantity
    total_product=0    
    for quantities in cart_product:
        total_product =total_product+quantities.quantity
    context = {
        'category': category,        
        'comment': comment,
        'total_amount':total_amount,               
        'total_product':total_product,

    }
    return render(request, 'usercomment.html', context)


def comment_delete(request, id):
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id, id=id)
    comment.delete()
    messages.success(request, 'Your comment is successfully deleted')
    return redirect('usercomment')    





    