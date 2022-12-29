from django.urls import path
from app1.views import *
app1_name='balu'

urlpatterns=[
    path('balu/',balu,name='balu'),
    path('bala/',bala,name='bala'),
]