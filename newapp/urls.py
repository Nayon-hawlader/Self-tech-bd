from django.urls import path
from .views import index, product_single, Add_to_Shoping_cart,Add_to_Shoping_cart_trend,Add_to_Shoping_cart_form,cart_details, cart_delete, OrderCart, comment_add,comment_trend,  Faq_details,chart_admin, SearchView, Blog_Post, Blog_single, Shop, Contact, Single_product_pro,Cashmemo


urlpatterns = [
    path('', index , name="index"),
    path('cart_details/', cart_details , name="cart_details"),
    path('product/<int:id>/',product_single, name='product_single'),
    path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path('addtrendcart/<int:id>/', Add_to_Shoping_cart_trend, name='Add_to_Shoping_cart_trend'),
    path('addcartform/<int:id>/', Add_to_Shoping_cart_form, name='Add_to_Shoping_cart_form'),
    path('cart_delete/<int:id>/',cart_delete, name='cart_delete'),    
    path('comment_add/<int:id>/',comment_add, name='comment_add'),
    path('comment_trend/<int:id>/',comment_trend, name='comment_trend'),

    path('oder_cart/', OrderCart, name="OrderCart"),
    path('Shop/', Shop, name="Shop"),
    path('faq/', Faq_details, name='Faq_details'),
    path('contact/', Contact, name='Contact'),
    path('chart_admin/', chart_admin, name='chart_admin'),
    path('search/',SearchView, name='search'),
    path('Blog_Post/',Blog_Post, name='Blog'),
    path('blog_single/<int:id>/',Blog_single, name='blog_single'),
    path('Cashmemo/',Cashmemo, name='Cashmemo'),
    
    path('single_product_pro/<int:id>/',Single_product_pro, name='single_product_pro'),


]
