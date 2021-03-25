from django.contrib import admin
from django.urls import path
from .views import placeorder,userlogout,customerwelcomeview,userauthenticate,userloginview,signupuser,adminloginview,adminhomepageview,authenticateadmin,logoutadmin,addpizza,deletepizza,homepageview


urlpatterns = [
	path('admin/',adminloginview,name='adminloginpage'),
	path('authenticateadmin/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name='adminhomepage'),
    path('logoutadmin/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('',homepageview, name='homepage'),
    path('signupuser/', signupuser),
    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/welcome/', customerwelcomeview, name='customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/', userlogout),
    path('placeorder/', placeorder),
]
