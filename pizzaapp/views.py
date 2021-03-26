from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel, CustomerModel, OrderModel
from django.contrib.auth.models import User
# Create your views here.
def adminloginview(request):
	return render(request, "pizzaapp/adminlogin.html")


def authenticateadmin(request):
	username=request.POST['username']
	password=request.POST['password']

	user = authenticate(username=username, password=password)

	#user exists

	if user is not None and user.username=="admin":
		login(request,user)
		return redirect('adminhomepage')
	#user doesnot exists
	if user is None:
		messages.add_message(request,messages.ERROR, "Invalid Credentials")
		return redirect('adminloginpage')

def adminhomepageview(request):
	context = {'pizzas':PizzaModel.objects.all()}
	return render(request, "pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
	name = request.POST['pizza']
	price = request.POST['price']
	PizzaModel(name = name, price = price).save()
	return redirect('adminhomepage')

def deletepizza(request,pizzapk):
	PizzaModel.objects.filter(id=pizzapk).delete()
	return redirect('adminhomepage')

def homepageview(request):
	return render(request,"pizzaapp/homepage.html")

def signupuser(request):
	username=request.POST['username']
	password=request.POST['password']
	phoneno=request.POST['phoneno']
	#if username already exist
	if User.objects.filter(username=username).exists():
		messages.add_message(request, messages.ERROR, "user already exist")
	# if username doesnot exist alredy
	User.objects.create_user(username=username, password=password).save()
	lastobject = len(User.objects.all())-1
	CustomerModel(userid=User.objects.all()[int(lastobject)].id, phoneno=phoneno)
	messages.add_message(request, messages.ERROR, "user  register successfully !")
	return redirect('homepage')


def userloginview(request):
	return render(request, "pizzaapp/userlogin.html")

def userauthenticate(request):
	username=request.POST['username']
	password=request.POST['password']

	user = authenticate(username=username, password=password)

	#user exists

	if user is not None:
		login(request,user)
		return redirect('customerpage')
	#user doesnot exists
	if user is None:
		messages.add_message(request,messages.ERROR, "Invalid Credentials")
		return redirect('userloginpage')

def customerwelcomeview(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	context = {'username': username, 'pizzas':PizzaModel.objects.all()}
	return render(request, "pizzaapp/customerwelcome.html", context)
def userlogout(request):
	logout(request)
	return redirect('userloginpage')

def placeorder(request):
	username= request.user.username
	phoneno= CustomerModel.objects.filter(userid=request.user.id)
	address= request.POST['address']
	orderitems= " "
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		name = pizza.name
		price = pizza.price
		quantity=request.POST.get(str(pizzaid), " ")
		if str(quantity) != "0" and str(quantity) != " ":
			orderitems = orderitems + name + " " + price + " " +"quantity:" + quantity + " "
	#print(orderitems)
	OrderModel(username=username, phoneno=phoneno, address=address, orderitems=orderitems)
	messages.add_message(request, messages.ERROR, "Order Successfully placed")
	return redirect('customerpage')

