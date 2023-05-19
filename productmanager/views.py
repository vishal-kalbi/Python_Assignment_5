from django.shortcuts import render,redirect,HttpResponse
from .models import *
from adminn.models import *

# Create your views here.
def index(request):
    u1 = ProdcutSubCategory.objects.all()
    return render(request,'index2.html',{"sss":u1})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        if username == 'Admin':
            request.session['username'] = username
            return redirect('admin_index')  # Redirect to the admin index URL
        else:
            request.session['username'] = username
            return redirect('index') # Redirect to the product manager index URL
      
def search(request):
    u1=ProdcutSubCategory.objects.filter(product__name__icontains = request.GET['search'])
        # u2=ProdcutSubCategory.objects.filter(name=request.POST['search'])
    return render(request,"index2.html", {"sec":u1})
    # else:
    #     return render(request,"index2.html",{"msgg":"product not found"})
    

    


def logout(request):
    # del request.session['username'] = username
    return redirect("login")
   
         