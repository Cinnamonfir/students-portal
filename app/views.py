from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Studentform
from django.template import loader
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'index.html', context)
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('')
    
def add(request):
    form = Studentform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('')
    
    context = {'form': form}
    return render(request, 'add.html', context)


def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('')
        else:
            messages.info(request, 'Incorrect password')
            
    return render(request, 'register.html')





def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.info(request, 'Invalid username')
            return redirect('login')
    else:    
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('')
