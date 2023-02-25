from django.urls import path
from . import views 
from .views import *


urlpatterns = [
    path('', views.home , name='home'),
    path('About', views.about , name='about'),
    path('Contact_Us', views.Contact , name='Contact'),
    path('Farming_Basics', views.BasicFarming , name='Basic_Farming'),
    path('Farming_Equpement', views.Eq_Farming , name='Equpement_Farming'),
    path('Farming_Products', views.ProductFraming , name='Products_Farming'),
    path('Farming_Types', views.GuideFarming , name='Types_of_Farming'),
    path('Farming_Scheme', views.Schemes, name='Scheme_Farming'),
    path('<slug:slug>', views.Full_Details , name='Full_Details'),
    path('search/', views.search, name='search'),

]
