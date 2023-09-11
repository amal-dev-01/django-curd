from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import Employee

# Create your views here.


def emp_list(request):
    context={'emp_list':Employee.objects.all()}
    return render(request,'emp_list.html',context)

def emp_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form=EmpForm()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmpForm(instance=employee)
        return render(request,'emp_form.html',{'form':form})
    else:
        if id == 0:
            form=EmpForm(request.POST)
        else:   
            employee=Employee.objects.get(pk=id)
            form=EmpForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')
    
def emp_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')