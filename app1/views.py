from django.shortcuts import render

# Create your views here.
def balu(request):
    d={'name':'balu','age':22}
    return render(request,'balu.html',d)


def bala(request):
    d={'name':'raviteja','movies':65}
    return render(request,'bala.html',d)