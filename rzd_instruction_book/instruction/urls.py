from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('instruction/', views.instruction_page, name='instruction'),
    path('show_inst/<slug:inst_slug>/', views.instruction_show, name='instruction_show'),
    path('scheme/', views.scheme_page, name='scheme'),
    path('show_scheme/<slug:scheme_slug>/', views.scheme_show, name='scheme_show'),
    path('malfunctions/', views.malfunctions_page, name='malfunctions'),
    path('show_malfunctions/<slug:malfunctions_slug>', views.malfunctions_show, name='malfunctions_show'),


]