from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import supplier_required,customer_required
from accounts.models import User,Counties
from business.models import Products
from business.forms import ProductsAddForm
from accounts.models import Categories,Supplier
from django.core.serializers import serialize


@login_required
def mainPageView(request):
    prod_obj=Products.objects.filter(user=request.user)
    sup=Supplier.objects.all()
    if request.user.is_supplier:
        prod_obj=Products.objects.filter(user=request.user)
    else:
        sup=Supplier.objects.all()
    context={
    'prod_obj':prod_obj,
    'sup':sup
    }
    return render(request,'business/mainPage.html',context)


#===================================Geo=========================================
def CountyView(request):
    counties=serialize('geojson',Counties.objects.all())
    return HttpResponse(counties,content_type='json')
def SupplierData(request):
    supply=serialize('geojson',Supplier.objects.all())
    return HttpResponse(supply,content_type='json')












#===============================================================================
def MySupplier(request,id):
    Mysup=Supplier.objects.get(id=id)
    context={
    'Mysup':Mysup
    }
    return render(request,'business/Mysupplier.html',context)
def SupplierCountyView(request):
    supcounties=serialize('geojson',Counties.objects.all())
    return HttpResponse(supcounties,content_type='json')
def SupDataView(request):
    supData=serialize('geojson',Supplier.objects.all())
    return HttpResponse(supData,content_type='json')



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
@login_required
@supplier_required
def ProductDelete(request,id):
    delete_product=Products.objects.get(id=id)
    delete_product.delete()
    return HttpResponseRedirect('/business/mainPage/')
