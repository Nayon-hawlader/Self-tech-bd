from typing import Text
from django import forms
from django.db import models
from django.utils import tree
from django.utils.html import mark_safe
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.db.models import Count, Sum, Avg, fields
from django.template.defaultfilters import truncatechars
import datetime, time
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django_cleanup import cleanup




class Banner(models.Model):
    id=models.AutoField(primary_key=True)
    banner_title = models.CharField(max_length = 50, blank=False)
    product_price_before = models.IntegerField(blank=True, null=True)
    current_price = models.IntegerField(blank=True, null=True)
    brand_name = models.CharField(max_length = 50, blank=False)
    banner_background = models.ImageField(("banner_background"),upload_to='banner_background/', blank=False)
    product_photo = models.ImageField(("banner_product_photo"),upload_to='banner_product_photo/', default='../placeholder.png', blank=True)
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
   
    def admin_photo(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.product_photo.url))
    admin_photo.short_description = "Image"
    admin_photo.allow_tags = True    

    def __str__(self):
        return f'{self.banner_title} {self.current_price} {self.product_add_date_time}'


class Deals_of_the_Week(models.Model):
    id = models.AutoField(primary_key=True)
    product_category =  models.CharField(max_length = 50, blank=False)
    product_price = MoneyField(decimal_places=0,default=0, default_currency='USD',max_digits=11,)
    brand_name = models.CharField(max_length = 50, blank=False)
    deal_price = MoneyField(decimal_places=0,default=0, default_currency='USD',max_digits=11,)
    availablity = models.CharField(max_length = 50, blank=False)
    available_number = models.IntegerField(blank=True, null=True)
    already_sold = models.IntegerField(blank=True, null=True)
    product_photo = models.ImageField(("Deals_of_the_Week_photo"),upload_to='Deals_of_the_Week_photo/', default='../placeholder.png', blank=True)
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
   
    def admin_photo(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.product_photo.url))
    admin_photo.short_description = "Deals_of_the_Week"
    admin_photo.allow_tags = True 

    def __str__(self):
        return f'{self.id} {self.product_category} {self.product_price} {self.deal_price}{self.availablity}{self.product_add_date_time}{self.product_photo}'


class Featured_product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    id = models.AutoField(primary_key=True)
    product_category =  models.CharField(max_length = 50,default="", blank=False)
    brand_name = models.CharField(max_length = 50, blank=False)
    product_description = models.CharField(max_length = 300,default="", blank=False)
    current_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    product_price_before = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField(default=0)
    new = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    product_photo_main = models.ImageField(("product_photo_main"),upload_to='Featured_product_photo/', default='../placeholder.png', blank=True)
    product_slider_photo_color_merun = models.ImageField(("product_slider_photo_color_merun"),upload_to='c/', default='../placeholder.png', blank=True)
    product_slider_photo_color_black = models.ImageField(("product_slider_photo_color_black"),upload_to='Featured_product_photo/', default='../placeholder.png', blank=True)
    product_slider_photo_color_silver = models.ImageField(("product_slider_photo_color_silver"),upload_to='Featured_product_photo/', default='../placeholder.png', blank=True)
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
    

        
    def admin_photo(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.product_photo_main.url))
    admin_photo.short_description = "Featured_Photo"
    admin_photo.allow_tags = True 

    def image(self):
        if self.product_photo_main:
            return self.product_photo_main.url
        else:
            return ""
    # deciaml_places
    # def save(self, *args, **kwargs):
    #     self.product_price_before = round(self.product_price_before, 2)
    #     super(Featured_product, self).save(*args, **kwargs)

    # def save_two(self, *args, **kwargs):
    #     self.current_price = round(self.current_price, 2)
    #     super(Featured_product, self).save(*args, **kwargs)
    def total_discount(self):
        return ((self.product_price_before - self.current_price)/self.product_price_before)*100
  
    def average_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(average=Avg('rate'))
        avgint_get = 0
        if reviews['average'] is not None:
            avgint_get = float(reviews['average'])
            avgint_get = avgint_get
            avgint_get = int(avgint_get)+1.0 
            avgint_get=int(avgint_get)  
            return avgint_get
        else:
            return avgint_get

    


    
        

    @property
    def short_description(self):
        return truncatechars(self.product_description, 35)

    def total_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = (reviews['count'])
            return cnt


    def __str__(self):
        return f'{self.id}{self.product_category} {self.product_description} {self.brand_name} {self.current_price} {self.product_price_before} {self.product_add_date_time} {self.product_photo_main}'



 
class Featured_productForm(ModelForm):
    COLOR = (
        ('Default', 'Default'),
        ('Gray', 'Gray'),
        ('Orchid', 'Orchid'),
        ('Hotpink', 'Hotpink'),
        ('Navy', 'Navy'),
    )
    color = forms.ChoiceField(choices=COLOR,widget=forms.RadioSelect)
    class Meta:
        model= Featured_product
        fields = ['color']

class Trend(models.Model):
    
    id = models.AutoField(primary_key=True)
    product_category =  models.CharField(max_length = 50,default="", blank=False)
    brand_name = models.CharField(max_length = 50, blank=False)
    product_description = models.CharField(max_length = 300,default="", blank=False)
    current_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    product_price_before = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField(default=0)
    new = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    product_photo_main = models.ImageField(("trends_photo"),upload_to='trends_photo/', default='../trends_1.jpg', blank=True)  
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.id}{self.product_category} {self.product_description} {self.brand_name} {self.current_price} {self.product_price_before} {self.product_add_date_time} {self.product_photo_main}'

    def Image(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.product_photo_main.url))
    Image.short_description = "Featured_Photo"
    Image.allow_tags = True 


    @property
    def short_description(self):
        return truncatechars(self.product_description, 25)

    def total_review(self):
        reviews = Comment.objects.filter(
            product_trend=self, status=True).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = (reviews['count'])
            return cnt
    def total_discount(self):
        return ((self.product_price_before - self.current_price)/self.product_price_before)*100
  
    def average_reviews(self):
        reviews = Comment.objects.filter(
            product_trend=self, status=True).aggregate(average=Avg('rate'))
        avgint_gets = 0
        if reviews['average'] is not None:
            avgint_gets = float(reviews['average'])
            avgint_gets = avgint_gets
            avgint_gets = int(avgint_gets)+1.0 
            avgint_gets=int(avgint_gets)  
            return avgint_gets
        else:
            return avgint_gets



class NewArrival(models.Model):
    
    id = models.AutoField(primary_key=True)
    product_category =  models.CharField(max_length = 50,default="", blank=False)
    brand_name = models.CharField(max_length = 50, blank=False)
    product_description = models.CharField(max_length = 300,default="", blank=False)
    current_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    product_price_before = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField(default=0)
    new = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    product_photo_main = models.ImageField(("NewArrival"),upload_to='NewArrival_photo/', default='../trends_1.jpg', blank=True)  
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return f'{self.id}{self.product_category} {self.product_description} {self.brand_name} {self.current_price} {self.product_price_before} {self.product_add_date_time} {self.product_photo_main}'
   
    @property
    def short_description(self):
        return truncatechars(self.product_description, 15)
   
   
    def Image(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.product_photo_main.url))
    Image.short_description = "NewArrival_Photo"
    Image.allow_tags = True 



class ShopCart(models.Model):
    id = models.AutoField(primary_key=True)
    p_id=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    brand_name =models.CharField(max_length=20, blank=True)
    color =models.CharField(max_length=20,default='Default')    
    current_price = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    quantity = models.IntegerField()
    amount= models.IntegerField()    
    section = models.CharField(max_length=15, blank=True)  
    product_photo_main = models.ImageField(("shopcart_image"),upload_to='shopcart_image', default='trends_photo/best_5.png')
    product_add_date_time = models.DateTimeField(auto_now_add=True, null=True)
    

    def amount(self):
        return self.quantity*self.current_price

    def image(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.product_photo_main.url))
    image.short_description = 'Image'
    image.allow_tags = True  
    
    @property
    def Datetime(self):
        return truncatechars(self.product_add_date_time, 20)
    



class ShopingCartForm(ModelForm):
    class Meta:
        model= ShopCart
        fields = ['quantity','color']            

    






class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, editable=False)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    total = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=20, default='New')
    ip = models.CharField(max_length=200, blank=True)
    adminnote = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    create_date = models.DateField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True)
    gift = models.BooleanField(default=False)
    product_photo_main = models.ImageField(("order_image"),upload_to='order_image', default='trends_photo/best_5.png')
    email = models.EmailField(max_length = 254, default="nayonhawlader.bd@gmail.com")

    
    def __str__(self):
        return f'{self.id}{self.user}{self.user.first_name}{self.last_name}{self.code}{self.phone}{self.address}{self.city}{self.country}{self.total}{self.status}{self.ip}{self.adminnote}{self.created_at}{self.update_at}{self.gift}'


# access function under save model function
    # def Gift_wrap(self):
    #     orders = self.Order_Time()
    #     return orders

    # def Total_Amount(self):
    #     return self.total+50    
    # def Gift_wrap(self):
    #     ntm = OderProduct.objects.all()
    #     if self.total%ntm.price == 70:
    #         return True

    def Order_Time(self):
        return self.created_at

    def sum(self):               
        items = Order.objects.all()
        total_price=0
        total_price = sum(items.values_list('total', flat=True,))
        total_price = '{:0.2f}'.format(total_price)
        return total_price

    


    total.allow_tags = True

        # if itemss -self.total !=50:
        #     return True
        # else:
        #     return False       
        
    

    
    



    # def __str__(self):
    #     return self.qr_code

    # def image_tag(self):
    #     return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.transaction_image.url))
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True   


class OderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name','email','phone','gift','address', 'city', 'country']


class OderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    p_id = models.IntegerField(default=0)
    user =models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField(default=0)
    total_amount = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=20, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    color =models.CharField(max_length=20,default='Default')
    product_photo_main = models.ImageField(("order_product_image"),upload_to='order_product_image', default='trends_photo/best_5.png')
    brand_name =models.CharField(max_length=20, blank=True)
    section =models.CharField(max_length=20,default='')
    qr_name = models.CharField(max_length=200, blank=True)
    qr_code = models.ImageField(upload_to='qr_code', blank=True)
    user_address = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length = 254, default="nayonhawlader.bd@gmail.com")
    
    @property    
    def code(self):
        return self.order.code
        
    @property
    def gift(self):
        return self.order.gift
   



    



    def order_product_photo(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.product_photo_main.url))
    order_product_photo.short_description = 'Image'
    order_product_photo.allow_tags = True   

    @property
    def short_description(self):
        return truncatechars(self.product, 35)
 
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.qr_name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.qr_name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save = False)
        canvas.close()
        super().save(*args, **kwargs)

    def get_image(self):
        if self.qr_code and hasattr(self.qr_code, 'url'):
            return self.qr_code.url
        else:
            return '/path/to/default/image'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),

    )
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Featured_product, on_delete=models.CASCADE, default='', blank=True, null=True )
    product_trend = models.ForeignKey(Trend, on_delete=models.CASCADE, default='', blank=True, null=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id=models.PositiveIntegerField(default=1)
    brand_name = models.CharField(max_length=200, blank=True)
    section = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=200, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    

    def __str__(self):
        return f'{self.id}{self.brand_name}{self.section}{self.p_id}'


  
    
        
class CommenttForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['brand_name','section','subject', 'comment', 'rate']


class Blog(models.Model):
        
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=80, unique=True)
    quote =  models.TextField(max_length=100, unique=True, blank=True)
    quote_owner =  models.TextField(max_length=50, blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)    
    created_time = models.TimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)    
    image = models.ImageField(("blog_image"),upload_to='blog_image/', default='blog_image/top_baner4.jpg', blank=True)
    
   
   
    def __str__(self):
        return f'{self.id}{self.updated_on}{self.status}{self.author}{self.quote_owner}'

    

    @property
    def short_description(self):
        return truncatechars(self.title, 25)
    @property
    def short_description_two(self):
        return truncatechars(self.quote, 15)

    def blog_photo(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    blog_photo.short_description = 'Image'
    blog_photo.allow_tags = True       




class FAQ(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    id = models.AutoField(primary_key=True)
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(choices=STATUS, max_length=200, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Contact(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.IntegerField()
    message = models.TextField()
    status = models.CharField(choices=STATUS, max_length=20, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}{self.name}{self.email}{self.phone}{self.status}{self.created_at}'
    @property
    def short_message(self):
        return truncatechars(self.message, 15)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','message']        

  
class Name(models.Model):    
    username = models.CharField(max_length=25, null=True)
    first_name = models.CharField(max_length=25,null=True)
    last_name = models.CharField(max_length=25, null=True)
    total_spent = models.ForeignKey(Order, on_delete=models.CASCADE, default='', blank=True, null=True )
    total_spentt = models.ForeignKey(Featured_product, on_delete=models.CASCADE, default='', blank=True, null=True )
    total_spenttt = models.ForeignKey(Trend, on_delete=models.CASCADE, default='', blank=True, null=True )
    ranking = models.CharField(max_length=25, null=True)
    phone = models.IntegerField(default="+880")
  
           
    
   
              
        

    def __str__(self):
        return f'{self.username}{self.first_name}{self.last_name}{self.total_spent}{self.ranking}'