from django.shortcuts import render
def login_view(request):
    return render(request,'accounts/login.html')
def signup(request):
    return render(request,'accounts/signup.html')



# Create your views here.
