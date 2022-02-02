from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    
    #GET
    path('allusers',views.get_All_Users),
    path('allwspc',views.get_All_Workspaces),
    path('alltasks',views.get_All_Tasks),
    
    #POST
    path('add/',views.createWorkspace),
] 