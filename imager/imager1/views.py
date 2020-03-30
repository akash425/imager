from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html', {'uname':'us_name'})

def upload(request):
    return render(request, 'upload.html')

def add(request):

    val1=int(request.POST['a'])
    val2=int(request.POST['b'])
    res=val1+val2

    return render(request, 'result.html', {'result':res})