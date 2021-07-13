from django.urls import path
from UserApp.views import user_logout, user_login, user_register, userprofile, user_update, user_password, usercomment, comment_delete, track_order


from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

from django.contrib.auth import views as auth_views


from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView



urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('profile/', userprofile, name='userprofile'),
    path('user_update/', user_update, name='user_update'),
    path('password_update/', user_password, name="user_password"),
    path('user_comment/', usercomment, name="usercomment"),
    path('user_comment_delete/<int:id>/', comment_delete, name="comment_delete"),
    path('track_order/', track_order, name='track_order'),

    path('logout/', user_logout, name='user_logout'),


]
