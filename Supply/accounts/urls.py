from django.urls import path
from accounts import views
from accounts.views import SupplierSignupView,CustomerSignupView#importing a
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
app_name='accounts'


urlpatterns=[
path('',views.Home,name='home'),
path('supplier/',SupplierSignupView.as_view(),name='supplier'),
path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('customer/',CustomerSignupView.as_view(),name='customer'),
path('SupplierProfile/',views.SupplierProfileView,name="profile"),
path('CustomerProfile/',views.CustomerProfileView,name="profilecus"),
]
