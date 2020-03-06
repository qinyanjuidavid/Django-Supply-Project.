from django.urls import path
from business import views
app_name='business'

urlpatterns=[

path('mainPage/',views.mainPageView,name="main"),
path('addProduct/',views.ProductAddView,name="add"),
path('productDetails/<id>/',views.ProductDetailsView,name="detail"),
path('updateProduct/<id>/',views.UpdateProductView,name="update"),
path('productDelete/<id>/',views.ProductDelete,name="delete")
]
