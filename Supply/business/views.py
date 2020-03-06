from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import supplier_required,customer_required
from accounts.models import User
from business.models import Products
from business.forms import ProductsAddForm



@login_required
def mainPageView(request):
    if request.user.is_supplier:
        prod_obj=Products.objects.filter(user=request.user)
    context={
    'prod_obj':prod_obj
    }
    return render(request,'business/mainPage.html',context)
@login_required
@supplier_required
def ProductAddView(request):
    if request.method=="POST":
        form=ProductsAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            prod=form.save(commit=False)
            prod.user=request.user
            prod.save()
            return HttpResponseRedirect('/business/mainPage/')
    else:
        form=ProductsAddForm()
    context={
    'form':form
    }
    return render(request,'business/ProductAdd.html',context)
@login_required
@supplier_required
def ProductDetailsView(request,id):
    product_details=Products.objects.get(id=id)
    context={
    'product_details':product_details
    }
    return render(request,'business/productDetails.html',context)
@login_required
@supplier_required
def UpdateProductView(request,id):
    product_update=Products.objects.get(id=id)
    form=ProductsAddForm(instance=product_update)
    if request.method=="POST":
        form=ProductsAddForm(request.POST or None,request.FILES or None,instance=product_update)
        if form.is_valid():
            form.save()
    context={
    'form':form
    }
    return render(request,'business/UpdateProduct.html',context)
def ProductDelete(request,id):
    delete_product=Products.objects.get(id=id)
    delete_product.delete()
    return HttpResponseRedirect('/business/mainPage/')
