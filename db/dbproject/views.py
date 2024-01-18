from django.shortcuts import render
from .models import product
from .models import product_details
import cx_Oracle
from datetime import datetime as dt

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index.html')
def display(request):
    return render(request,'displayresult.html')
def about(request):
    return render(request,'about.html')
def register(request):
    pname1=request.POST.get('pname')
    pname1=str(pname1).upper()
    pquantity1 = request.POST.get('pquantity')
    pprice=request.POST.get('pprice')
    ptype=request.POST.get('ptype')


    if pname1 == '' or pquantity1 == '' or pprice == '' or ptype == None :
        params={'d':'you must have to fill all the data'}
        return render(request,'index.html',params)

    elif pquantity1!='' and pprice!='' and str(pquantity1).isdigit() and str(pprice).isdigit():
        if ptype == 'Purchases':
            data = product(pname=pname1, pquantity=pquantity1, pprice=pprice, ptype=ptype)
            data.save()
            cart = product_details.objects.filter(pname=pname1)
            if len(cart)==0:
                data1 = product_details(pname=pname1, pquantity=pquantity1)
                data1.save()
                return render(request, 'registrationsuccess.html')
            else:
                for i in cart:
                    x = int(i.pquantity) + int(pquantity1)
                    dtime = dt.now()
                    date = dtime.strftime("%Y-%m-%d")
                    product_details.objects.filter(pname=pname1).update(pquantity=x,pudate=date)
                return render(request, 'registrationsuccess.html')
        else:
            cart1 = product_details.objects.filter(pname=pname1)
            for j in cart1:
                qn = int(j.pquantity)
                y = qn-int(pquantity1)
                if int(pquantity1)<qn:
                    product_details.objects.filter(pname=pname1).update(pquantity=y)
                    data = product(pname=pname1, pquantity=pquantity1, pprice=pprice, ptype=ptype)
                    data.save()
                    return render(request, 'registrationsuccess.html')
                else:
                    params = {'d': 'The product Quantity is less Please Decrease the Quantity'}
                    return render(request, 'index.html', params)
            else:
                params = {'d': 'The product is not avaliable for sales'}
                return render(request, 'index.html', params)
    else:
        if pquantity1!='' and pprice!=''and str(pquantity1).isdigit()==False and str(pprice).isdigit()==False:
            params = {'d': 'Please check the Product Quantity, Product Price and enter Numeric value.'}
            return render(request, 'index.html', params)
        elif pquantity1!='' and str(pquantity1).isdigit()==False:
            params = {'d': 'Please check the Product Quantity and enter Numeric value.'}
            return render(request, 'index.html', params)
        elif pprice!='' and str(pprice).isdigit()==False:
            params = {'d': 'Please check the Product Price and enter Numeric value.'}
            return render(request, 'index.html', params)
def registermore(request):
    return render(request,'index.html')

def result(request):
    date=request.POST.get('date')
    if date == '':
        params1={'d':'Please you must have choose the date'}
        return render(request,'displayresult.html',params1)
    else:
        all_data=product.objects.filter(pdate=date)
        params={'all':all_data}
        return render(request, 'result.html',params)

def search(request):
    search=request.POST.get('search')
    if search == '':
        return render(request, 'index.html')
    else:

        data =product_details.objects.filter(pname__icontains=search)
        params={'all':data}
        return render(request, 'search.html',params)


