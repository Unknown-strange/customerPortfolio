from django.urls import path
from . import views



urlpatterns = [ 
    path('', views.index, name='index'),  
    path('send-email/', views.send_to_org, name='send_to_org'),

]
