from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request,'index.html',{'students':Student.objects.all()})

#def view_student(request, id):
#    student=Student.objects.get(pk=id)
#    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    form=StudentForm()
    if request.POST:
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'add.html',{'form':StudentForm(),'success':True})

        else:
            form=StudentForm()
    return render(request,'add.html',{'form':form})

def edit(request,id):
    instance_to_edit=Student.objects.get(pk=id)
    if request.POST:
        form=StudentForm(request.POST,instance=instance_to_edit)
        if form.is_valid():
            instance_to_edit.save()
            return render(request,'edit.html',{'form':form,'success':True})
    else:
        form=StudentForm(instance=instance_to_edit)
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    instance=Student.objects.get(pk=id)
    instance.delete()
    return render(request,'index.html',{'success_message': 'Student deleted successfully'})
            

#def views_page(request):
#    student_id = request.GET.get('id')  # Retrieve student ID from URL parameter
#    student = get_object_or_404(Student, pk=student_id)  # Fetch student details
#    return render(request, 'views.html', {'student': student})