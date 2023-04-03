from django.urls import path
from . import views

urlpatterns = [
        path('',views.view),
        path('home1',views.view),
        path('reg',views.register),
        path('registered',views.existing),
        path('search',views.search),
        path('drop',views.dropout),
       
]
