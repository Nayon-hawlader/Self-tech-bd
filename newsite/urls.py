from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import handler404, url
from newapp.views import handle_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),
    path('user/', include('UserApp.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




handler404 = "newapp.views.handle_not_found"