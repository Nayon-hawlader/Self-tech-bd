import django
from django.contrib import admin
from django.http import response
from django.utils.html import format_html
import decimal, csv
from django.http import HttpResponse
from django.db.models import F
admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.__path__[0] + "/templates/admin/base_site.html"

from .models import*


admin.site.site_header = "My admin"
admin.site.site_title = "Site admin portal"
admin.site.index_title = "Welcome to site admin portal"



class BannerAdmin(admin.ModelAdmin):

    list_display = ('banner_title','brand_name','current_price','product_add_date_time','admin_photo')

class Deals_of_the_Week_Admin(admin.ModelAdmin):

    list_display = ('id','product_category', 'brand_name','product_price','deal_price','availablity', 'available_number', 'already_sold', 'product_add_date_time', 'admin_photo')

def export_price(modeladmin, request, queryset):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = "price.csv"'
    writer = csv.writer(response)
    writer.writerow(['amount', 'brand_name', 'comment', 'current_price', 'discount', 'id', 'new', 'oderproduct', 'product_add_date_time', 'product_category', 'product_description', 'product_photo_main', 'product_price_before', 'product_slider_photo_color_black', 'product_slider_photo_color_merun', 'product_slider_photo_color_silver', 'shopcart'])
    product = queryset.values_list('amount', 'brand_name', 'comment', 'current_price', 'discount', 'id', 'new', 'oderproduct', 'product_add_date_time', 'product_category', 'product_description', 'product_photo_main', 'product_price_before', 'product_slider_photo_color_black', 'product_slider_photo_color_merun', 'product_slider_photo_color_silver', 'shopcart')
    for products in product:
        writer.writerow(products)
    return response
export_price.short_description = "Export to csv"    



class Featured_productAdmin(admin.ModelAdmin):
    
    list_display = ('id','product_category','brand_name','short_description', 'current_price','product_price_before', 'new', 'discount', 'product_add_date_time', 'admin_photo')
    readonly_fields = ('amount',)
    actions=['apply_increse_six','apply_decrese_seven','apply_discount','apply_discount_two','apply_discount_three','apply_discount_four','apply_discount_five','apply_increse','apply_increse_two','apply_increse_three', export_price]
    list_filter = ['current_price']

    def apply_discount(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('0.9'))
    apply_discount.short_description = 'Apply 10%% discount'   
   
    def apply_discount_two(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('0.8'))
    apply_discount_two.short_description = 'Apply 20%% discount'   
   
    def apply_discount_three(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('0.7'))
    apply_discount_three.short_description = 'Apply 30%% discount'   
   
    def apply_discount_four(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('0.6'))
    apply_discount_four.short_description = 'Apply 40%% discount'   
  
    def apply_discount_five(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('0.5'))
    apply_discount_five.short_description = 'Apply 50%% discount'   
 
    def apply_increse(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('1.1'))
    apply_increse.short_description = 'Apply 10%% increse'

    def apply_increse_two(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('1.2'))
    apply_increse_two.short_description = 'Apply 20%% increse' 

    def apply_increse_three(self, request, queryset):
        queryset.update(current_price = F('current_price')*decimal.Decimal('1.3'))
    apply_increse_three.short_description = 'Apply 30%% increse'    
    
    def apply_increse_six(self, request, queryset):
        queryset.update(current_price = F('current_price')+10)
    apply_increse_six.short_description = 'Apply 10$ increse per product' 
    def apply_decrese_seven(self, request, queryset):
        queryset.update(current_price = F('current_price')-10)
    apply_decrese_seven.short_description = 'Apply 10$ decrese per product' 
# update every product value
# queryset.update(current_price = F('current_price')+10)

class TrendAdmin(admin.ModelAdmin):
    
    list_display = ('id','product_category','brand_name','short_description', 'current_price','product_price_before', 'new', 'discount', 'product_add_date_time', 'Image')
    readonly_fields = ('amount',)
    actions=['apply_increse_six','apply_decrese_seven', export_price]
    list_filter = ['current_price']


    def apply_increse_six(self, request, queryset):
        queryset.update(current_price = F('current_price')+10)
    apply_increse_six.short_description = 'Apply 10$ increse per product' 
    def apply_decrese_seven(self, request, queryset):
        queryset.update(current_price = F('current_price')-10)
    apply_decrese_seven.short_description = 'Apply 10$ decrese per product' 


class NewArrivalAdmin(admin.ModelAdmin):
    
    list_display = ('id','product_category','brand_name','short_description', 'current_price','product_price_before', 'new', 'discount', 'product_add_date_time', 'Image')
    readonly_fields = ('amount',)    
    list_filter = ['current_price']


class ShopCartAdmin(admin.ModelAdmin):

    list_display = ('id','user','p_id','brand_name','color','current_price','quantity','amount','section','Datetime','image')
    list_filter = ['user']




class OrderProductline(admin.TabularInline):
    model = OderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','code',
                    'phone', 'total','ranking','sum','gift', 'status', 'Order_Time','address','city']
    list_filter = ['status','gift','city']
    readonly_fields = ('user', 'first_name', 'last_name',
                       'phone', 'address', 'city', 'country', 'total', 'ip')
   
    can_delete = False
    search_fields=['user']
    # inlines = [OrderProductline]

    # list_editable = ['last_name']
    list_per_page = 15

    def ranking(self, obj):
        color_one = 'deepskyblue'
        color_two = 'cyan'
        color_three = 'cornflowerblue'
        color_four = 'gold'
        var_one = 'New'        
        var_two = 'Silver'        
        var_three = 'Gold'        
        var_four = 'Top Buyer'        
        if obj.total > 40 and obj.total < 500: 
            color_one = 'deepskyblue'
            return format_html('<b style="color:{};">{}</b>',color_one, var_one)
        elif obj.total > 500 and obj.total < 1000: 
            color_two = 'cyan'
            return format_html('<b style="color:{};">{}</b>',color_two, var_two)
        if obj.total > 1000 and obj.total < 2000: 
            color_three = 'cornflowerblue'
            return format_html('<b style="color:{};">{}</b>',color_three, var_three)
        if obj.total > 2000: 
            color_four = 'gold'
            return format_html('<b style="color:{};">{}</b>',color_four, var_four)

    



class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id','p_id','user_address','phone', 'brand_name','quantity', 'price','color', 'amount','total_amount','gift','code','status','section','order_product_photo']
    readonly_fields = ( 'brand_name', 'short_description', 'price', 'quantity', 'amount','order_product_photo')
      
  
    
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','p_id','brand_name','section','status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10
    actions=['True_all']

    def True_all(self, request, queryset):
        queryset.update(status=True)
    True_all.short_description = 'True All' 

admin.site.register(Comment, CommentAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','status','short_description_two','quote_owner' ,'short_description', 'slug', 'author','created_time','created_date','blog_photo']
    list_filter = ['status', 'created_date']
    list_per_page = 15


admin.site.register(Blog, BlogAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone' ,'status', 'short_message', 'created_at']
    list_filter = ['status', 'created_at']
    list_per_page = 15


admin.site.register(Contact, ContactAdmin)


    

admin.site.register(Banner, BannerAdmin)
admin.site.register(Deals_of_the_Week, Deals_of_the_Week_Admin)
admin.site.register(Featured_product, Featured_productAdmin)
admin.site.register(Trend, TrendAdmin)
admin.site.register(NewArrival, NewArrivalAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OderProduct, OrderProductAdmin)

class FAQAdamin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'created_at', 'updated_at']


admin.site.register(FAQ, FAQAdamin)


class NameAdmin(admin.ModelAdmin):
    list_display = ['total_spent','ranking','phone',]


admin.site.register(Name, NameAdmin)