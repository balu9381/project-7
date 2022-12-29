from django.shortcuts import render

# Create your views here.
def ravi(reuqest):
    d={'name':'balakullayappa','mobile':9381019929}
    return render(reuqest,'ravi.html',d)

def teja(reuqest):
    d={'name':'ravitja','moviename':'kick'}
    return render(reuqest,'teja.html',d)