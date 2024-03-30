from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request,'index.html',{'students':Student.objects.all()})

def view_student(request, id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    form=StudentForm()
    if request.POST:
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=StudentForm()
    return render(request,'add.html',{'form':form})

            

#def views_page(request):
#    student_id = request.GET.get('id')  # Retrieve student ID from URL parameter
#    student = get_object_or_404(Student, pk=student_id)  # Fetch student details
#    return render(request, 'views.html', {'student': student})