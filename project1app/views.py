from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from project1app.models import signuptable
from project1app.models import detailstable
from project1app.models import salarytable

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        # a=json.loads(request.body)
        print(request.POST.get('fname'))
        resp_obj=signuptable.objects.create(username=request.POST.get('uname'),
                                           password=request.POST.get('password'),
                                           email=request.POST.get('email'),
                                           mobilenumber=request.POST.get('mobilenumber'),
                                           firstname=request.POST.get('fname'),
                                           lastname=request.POST.get('lname')),

        b = {'message': "successfully created"}
        return redirect('details')

    return render(request,'signup.html')
def details(request):
    if request.method=="POST":
        resp_obj=detailstable.objects.create(username=request.POST.get('username'),
                                          login_time=request.POST.get('logintime'),
                                          logout_time=request.POST.get('logouttime'),
                                          status=request.POST.get('status'))

        return redirect('newpage')
    return render(request,'details.html')

def newpage(request):
    newpro=detailstable.objects.all()
    if request.method=="POST":
        condition=Q(status=1)
        user_term = request.POST.get('username')
        print(user_term)
        logout_term = request.POST.get('logouttime')
        print(logout_term)
        login_term = request.POST.get('logintime')
        print(login_term)
        status_term = request.POST.get('status')
        print(status_term)
        if user_term is not None or user_term=='':
            condition &=Q(username__icontains=user_term)
        if logout_term is not None or logout_term == '':
            condition &= Q(login_time__icontains=logout_term)
        if login_term is not None or login_term == '':
            condition &= Q(logout_time__icontains=logout_term)
        user = detailstable.objects.filter(condition)
        return render(request,'newpage.html',{'newdata':user})
    return render(request, 'newpage.html', {'newdata': newpro},)

def homepage(request):
    return render(request,'home.html')
def salaryD(request):
    if request.method=="POST":
        resp_obj=salarytable.objects.create(username=request.POST.get('username'),
                                          password=request.POST.get('password'),
                                          salary=request.POST.get('salary'),
                                          status=request.POST.get('status'),
                                          date=request.POST.get('date')),

        return redirect('salarypage')
    return render(request,'salaryD.html')

def salarypage(request):
    slrydetail = salarytable.objects.all()
    return render(request, 'salarypage.html', {'newdata': slrydetail}, )




