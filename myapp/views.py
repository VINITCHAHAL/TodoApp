from django.shortcuts import render , HttpResponse

# Create your views here.
def myapp(request):
    return HttpResponse("This is first")
