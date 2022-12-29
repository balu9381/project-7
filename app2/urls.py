from django.urls import path
from app2.views import *
app2_name='ravi'

urlpatterns=[
    path('ravi/',ravi,name='ravi'),
    path('teja/',teja,name='teja')
]