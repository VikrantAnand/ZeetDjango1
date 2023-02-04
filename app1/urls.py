from django.urls import path
from .views import *
urlpatterns = [
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',loginview,name='login'),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('form/',datapost,name='datapost'),
    path('view/<int:abc>/',productview,name='proview'),
    path('proall/',proall,name='proall'),
    path('search/',searchview,name='search'),
    path('del/<int:abc>/',productdelete,name='prodel'),
    path('logout/',logout,name='logout'),
    path('productadd/',productadd,name='productadd'),
    path('profile_manage/',profile_manage,name='profile'),
    path('addCustomer/',addCustomer,name='addC'),
    path('viewCustomer/',viewCustomer,name='viewC'),
    path('addProduct/',addProduct,name='addP'),
    path('viewProduct/',viewProduct,name='viewP'),
    path('deleteC/<int:abc>/',DeleteCustomer,name='DeleteCustomer'),
    path('deleteP/<int:abc>/',DeleteProduct,name='DeleteProduct'),
    path('updateP/<int:abc>/',UpdateProduct,name='UpdateProduct')
]