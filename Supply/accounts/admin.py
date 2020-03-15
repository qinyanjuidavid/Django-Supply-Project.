from django.contrib import admin
from accounts.models import User,Supplier,Customer,Categories,Counties
from accounts.forms import UserChangeForm,UserCreationForm
from leaflet.admin import LeafletGeoAdmin



class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','is_admin','is_staff','is_active','is_supplier','is_customer')
    list_filter=('is_admin','is_staff','is_active','is_supplier','is_customer')
    search_fields=['username','first_name','email','last_name']
    form=UserChangeForm
    add_form=UserCreationForm

class SupplierAdmin(LeafletGeoAdmin):
    list_display=('user','location')

admin.site.register(Supplier,SupplierAdmin)
class CountiesAdmin(LeafletGeoAdmin):
    list_display=('name','code')
admin.site.register(Counties,CountiesAdmin)
admin.site.register(Customer)
admin.site.register(Categories)
admin.site.register(User,UserAdmin)
