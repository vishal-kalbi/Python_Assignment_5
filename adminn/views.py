from django.shortcuts import render ,HttpResponse,redirect
from .models import *

# Create your views here.
def admin_index(request):

    if request.method=="GET":
        return render(request,'admin_index.html')
    else:

        Product.objects.create(
            name=request.POST['Product_name']
        )
        # request.session['Product_name'] = request.POST['Product_name']
        # return render(request,'admin_index.html)   
        u1=Product.objects.get(name=request.POST['Product_name'])
           
        ProdcutSubCategory.objects.create(
            price=request.POST['Product_price'],
            product_pic=request.FILES['Product_picture'],
            product_model=request.POST['Product_model'],
            product=u1
        )
        return render(request,"admin_index.html",{"msg":"product information added"})
        
          
def view_product(request):
   
    u2=ProdcutSubCategory.objects.all()

    return render(request,'view_product.html',{"userdata2":u2})

def delete(request,cid):
    c_obj = Product.objects.get(id = cid)
    c_obj.delete()
    return redirect('view_product')

def update_product(request):
    return render(request,"update_product.html")
    
    