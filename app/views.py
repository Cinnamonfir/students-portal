from django.shortcuts import render, redirect
from .models import Student
from django.template import loader
from .forms import Studentform
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    students = Student.objects.all()
    template = loader.get_template('index.html')
    context = {'students': students}    
    return HttpResponse(template.render(context, request))

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
