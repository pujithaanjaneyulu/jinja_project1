from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'pujitha','age':21}
    return render(request,'jinja print.html',context=d)
