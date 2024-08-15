from django import template
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse

from students.forms import StudentForm
from students.models import College, Student


def students(request):
    template = loader.get_template("student.html")
    students=Student.objects.all().values()
    context= {
        'students':students
    }
    return HttpResponse(template.render(context,request))

def createStudent(request):
    if request.method == 'GET':
        form = StudentForm()
        college = College.objects.all().values()
        return render(request,'createStudent.html',{'college':college, 'studentForm':form})

    elif request.method == 'POST':
        
        form = StudentForm(request.POST)
        if form.is_valid():
            rollNO = form.cleaned_data['rollNO']
            address = form.cleaned_data['address']
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            collegeID =form.cleaned_data['college']    
            college = College.objects.get(id = collegeID)
            print(rollNO, name, address, dob,collegeID)
            student ={
                'rollNO':rollNO,
                'name':name,
                'address':address,
                'dob':dob,
                'college':college
            }
    return redirect('students')

def viewStudent(request):
    template = loader.get_template("student.html")  # Fixed template reference
    students = Student.objects.all()
    context = {'students': students}
    return HttpResponse(template.render(context, request))