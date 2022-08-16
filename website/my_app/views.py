from ast import Return
from time import time
from urllib import response
from django.shortcuts import render, redirect,HttpResponseRedirect
from my_app.models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .forms import StudentRegistration


# Create your views here.





def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date =  request.POST.get('date')
        student = Student (
            name = name,
            description = description,
            date = date,

        )
        student.save()
    return render(request, 'index.html')


def home(request):
    task = Student.objects.all()
    return render(request,'home.html',{'task':task})


def updatedata(request,id):
    task = Student.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date =  request.POST.get('date')
        task = Student.objects.get(pk=id)
        task.name = name
        task.description = description
        task.date = date
        task.save()
    
    context = {
            "task":task
        }

    return render(request,'index.html',context)




def deletedata(request,id):
    if request.method == 'POST':
        task = Student.objects.get(pk=id)
        task.delete()
    return redirect('my_app:home')




@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'update':'/taskupdate/<str:pk>/',
        'delete':'/taskdelete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many= True) #python data

    return Response(serializer.data)


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
    else:
        fm = StudentRegistration()
    return render(request,'index.html',{'form':fm})