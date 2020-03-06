from django.contrib import admin
from accounts.models import User,Supplier,Customer,Products
from accounts.forms import UserChangeForm,UserCreationForm


class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','is_admin','is_staff','is_active','is_supplier','is_customer')
    list_filter=('is_admin','is_staff','is_active','is_supplier','is_customer')
    search_fields=['username','first_name','email','last_name']
    form=UserChangeForm
    add_form=UserCreationForm

admin.site.register(User,UserAdmin)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Products)
