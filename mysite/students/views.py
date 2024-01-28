from django.shortcuts import render ###HTML PAGE
from django.http import HttpResponse ## TO DISPLAY A MESSAGE
from .models import Student
# Create your views here.
def home(request):
    #return HttpResponse("Hello,This is my home page")
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        student = None
    return render (request, 'student.html', {'student': student})
    