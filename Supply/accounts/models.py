from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class custommanager(BaseUserManager):
    def create_user(self,email,username,password=None,is_active=True,is_staff=False,is_admin=False,is_supplier=False,is_customer=False):
        if not email:
            raise ValueError('Users must have an email.')
        if not password:
            raise ValueError('Users must have a password.')
        if not username:
            raise ValueError('Users must have a username.')
        user_obj=self.model(
        email=self.normalize_email(email),
        username=username
        )
        user_obj.set_password(password)
        user_obj.is_active=is_active
        user_obj.is_admin=is_admin
        user_obj.is_staff=is_staff
        user_obj.is_customer=is_customer
        user_obj.is_supplier=is_supplier
        user_obj.save(using=self._db)

        return user_obj
    def create_staff(self,email,username,password=None):
        user=self.create_user(
        email,
        username,
        password=password,
        is_staff=True,
        is_supplier=False,
        is_customer=False
        )
        return user
    def create_superuser(self,email,username,password=None):
        user=self.create_user(
        email,
        username,
        password=password,
        is_staff=True,
        is_admin=True,
        is_supplier=True,
        is_customer=True
        )
        return user
class User(AbstractBaseUser):
    username=models.CharField(max_length=255,verbose_name="Username",unique=True)
    first_name=models.CharField(max_length=256,blank=True,null=True)
    last_name=models.CharField(max_length=256,blank=True,null=True)
    email=models.EmailField(verbose_name='Email Address',max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_supplier=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=custommanager()

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def staff(self):
        return self.staff
    @property
    def admin(self):
        return self.admin
    @property
    def active(self):
        return self.active
    @property
    def supplier(self):
        return self.supplier
    @property
    def customer(self):
        return self.customer
class Products(models.Model):
    product_name=models.CharField(max_length=50)
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name_plural='Products'
class Supplier(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=20,blank=True,null=True)
    image=models.ImageField(upload_to='Supplier_Profile_picts',default="default.jpg")
    telephone=models.CharField(max_length=20,default="+254")
    status=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural="Suppliers"

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    interest=models.ManyToManyField(Products)
    image=models.ImageField(upload_to="Customer_profile_picts",default="default.jpg")
    status=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural='Customers'

'''@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if instance.is_supplier:
        profile,created=Supplier.objects.get_or_create(user=instance)
    else:
        Customer.objects,get_or_create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.is_customer:
        profile,created=Customer.objects.get_or_create(user=instance)

    else:
        Supplier.objects.get_or_create(user=instance)'''
