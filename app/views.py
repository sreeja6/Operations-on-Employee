from django.shortcuts import render,redirect
from app.models import Employee
from django.contrib import messages

def main(request):
    return render(request,"main.html")
def add_emp(request):
    return render(request, "add_emp.html")
def save_emp(request):
    id = request.POST.get("a1")
    name = request.POST.get("a2")
    sal = request.POST.get("a3")
    Employee(idno=id,name=name,salary=sal).save()
    messages.success(request,"Employee is added Sucessfully ")
    return redirect('main')
def view_all_emp(request):
    return render(request,"view_all_emp.html",{"emp":Employee.objects.all()})
def delete_emp(request):
    n = request.GET.get('no')
    res = Employee.objects.get(idno=n).delete()
    return redirect('view_all_emp')

def update_emp(request):
    u = request.GET.get("u1")
    res = Employee.objects.get(no=u)
    return render(request,"Update_page.html",{"update":res})
def updated(request):
    i = request.POST.get("ue1")
    na = request.POST.get("ue2")
    sal = request.POST.get("ue3")
    Employee.objects.filter(idno=i) .update(name=na,salary=sal)
    return redirect('view_all_emp')








