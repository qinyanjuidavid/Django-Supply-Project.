from django.urls import path
from business import views
app_name='business'

urlpatterns=[

path('mainPage/',views.mainPageView,name="main"),
path('addProduct/',views.ProductAddView,name="add"),
path('productDetails/<id>/',views.ProductDetailsView,name="detail"),
path('updateProduct/<id>/',views.UpdateProductView,name="update"),
path('productDelete/<id>/',views.ProductDelete,name="delete"),
path('supplier/<id>/',views.MySupplier,name='mysupplier'),
#=================================================
path('counties/',views.CountyView,name='county'),
path('supply/',views.SupplierData,name="supply"),

path('county/',views.SupplierCountyView,name='supCounty'),
path('supData/',views.SupDataView,name='supData')
]
