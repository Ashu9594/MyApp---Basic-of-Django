from django.shortcuts import render,HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html',{'dests':dests})

# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     res = val1+val2
#     return render(request, 'result.html',{'result':res})

def about(request):
    return render(request, 'about.html')

