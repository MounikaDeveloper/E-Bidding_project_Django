"""Bidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



from user import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer_seller/',TemplateView.as_view(template_name="users_template/login_register.html"),name="buyer_seller"),
    path('register/',views.registerUser,name="register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('home/',TemplateView.as_view(template_name="users_template/user_home.html"),name="user_home"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('sell_product/',views.sellproduct,name="sell_product"),
    path('productsave/',views.productsave,name="productsave"),
    path('removeproduct/',views.removeproduct,name="removeproduct")
]
