from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login

from authentication.models import Userprofile
from extras.models import ExtraItem

from .models import *
from authentication.views import *
from .forms import *

# Create your views here.

@login_required(login_url='login/')
def bill(request):
	total = 0
	items = Transaction.objects.filter(user = request.user)
	for item in items:
		total += item.price

	context = {
	'total' : total,
	'transactions' : items
	}
	return render(request, 'bill.html', context)


@login_required(login_url='login/')
def home(request):
	context = {
			'menu' : ExtraItem.objects.all()
	}
	return render(request, 'home.html', context)


@login_required(login_url = 'login/')
@user_passes_test(is_member)
def admin_home(request):
	context = {
		'menu' : ExtraItem.objects.all()
	}
	return render(request,'admin_home.html',context)

@login_required(login_url = 'login/')
@user_passes_test(is_member)
def add_transaction(request):
	if request.method == 'POST':
		form = AddTransactionForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			regnum = userObj['regnum']
			number = userObj['number']
			item = userObj['item']
			customer = Userprofile.objects.filter(regNum = regnum)
			customer = customer.first()
			u = User.objects.filter(username = customer.user)
			u = u.first()
			order = ExtraItem.objects.filter(item_name = item)
			order = order.first()
			transaction = Transaction.objects.create(user = u, item = order)
			transaction.regNum = regnum
			transaction.number = number
			transaction.price = order.price * number
			transaction.save()
			return redirect('/home/admin/add')
		
		else:
			return render(request, 'register.html',{'error': 'There was an error! Please try again.', 'form' : form})



	else:
		form = AddTransactionForm()
	return render(request,'add_transaction.html',{'form':form})

@login_required(login_url = 'login/')
@user_passes_test(is_member)
def transactions(request):
	context = {
		'trans' : Transaction.objects.all()
	}
	return render(request,'transactions.html',context)

@login_required(login_url = 'login/')
@user_passes_test(is_member)
def remove_order(request,order_id):
	t = int(order_id)
	order = Transaction.objects.filter(id = t)
	order.delete()
	return redirect('/home/admin/prev')

