from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .form import *


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	# total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	Out_for_delivery = orders.filter(status='Out for delivery').count()

	context = {
		'orders':orders, 
		'customers':customers,
	    'total_orders':total_orders,
		'delivered':delivered,
		'Out_for_delivery' : Out_for_delivery,
	    'pending':pending 
	}

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_text):
    customer = Customer.objects.get(id=pk_text)
    orders = customer.order_set.all()

    order_count = orders.count()
    
    context = {
		'customer':customer,
		'orders':orders, 
		'order_count':order_count
	}
    return render(request, 'accounts/customer.html',context)

def create_order(request):
    form = Orderform()

    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
	        form.save()
	        return redirect('/')

    context = {
		'form':form
	}

    return render(request, 'accounts/form.html', context)


def update_order(request, pk_text):
    
    order = Order.objects.get(id=pk_text)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)


def delete_order(request, pk_text):
    order = Order.objects.get(id=pk_text)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item' : order
    }
    return render(request, 'accounts/delete.html', context)


def create_customer(request):
    form = Customerform()

    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
	        form.save()
	        return redirect('/')

    context = {
		'form':form
	}
    return render(request, 'accounts/form.html', context)


def update_customer(request, pk_text):
    customer = Customer.objects.get(id=pk_text)
    form = Customerform(instance=customer)
    if request.method == 'POST':
        form = Customerform(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)

def delete_customer(request, pk_text):
    customer = Customer.objects.get(id= pk_text)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {
        'item' : customer
    }
    return render(request, 'accounts/delete.html', context)


def customer_order(request, pk_text):
    Orderformset = inlineformset_factory(Customer, Order, fields=('product', 'status' ))
    customer = Customer.objects.get(id= pk_text)
    # form = Orderform(initial={'customer':customer})
    formset = Orderformset(instance=customer)
    if request.method == 'POST':
        # form = Orderform(request.POST)
        formset = Orderformset(request.POST, instance=customer)
        if formset.is_valid():
	        formset.save()
	        return redirect('/')

    context = {
		'formset':formset
	}
    return render(request, 'accounts/customer_form.html', context)