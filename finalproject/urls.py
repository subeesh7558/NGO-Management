from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('welfare', views.welfare, name="welfare"),
    path('', include('welfare.urls')),
    
    # path('ngoo/', views.ngo, name="ngoo"),
    # path('ngo/', include('ngo.urls')),

    # path('m/', views.main, name="m"),
    # path('main/', include('main.urls')), 

]
