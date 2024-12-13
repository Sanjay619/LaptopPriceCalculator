from django.shortcuts import render

# Create your views here.

def loginView(request):
    return render(request, 'login.html')

def SignUpView(request):
     return render(request, 'signup.html')

# def DashboardView(request):
#     pass
