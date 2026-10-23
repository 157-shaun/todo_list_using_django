from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.models import ToDos
# Create your views here.



def TestResponse(request):
    return HttpResponse("Hello developers, Welcome")

def home(request):
    
    if request.method=="POST":
        task_data=request.POST["task_name"]
        ToDos(task=task_data).save()
    my_tasks=ToDos.objects.all()
    is_authenticated=False
    context={"tasks":my_tasks, "status":is_authenticated}
    return render(request, "index.html",context)

def editTask(request,task_id):
    task=ToDos.objects.get(id=task_id)
    if request.method=="POST":
        task_data=request.POST["task_name"]
        status=request.POST.get("status",False)
        if status:
            task.is_completed=status.capitalize()
        else:
            task.is_completed=status
        task.task=task_data
        task.save()
        return redirect("/")
    return render(request,"edit_task.html",{"mytask":task})

def deleteTask(request, task_id):
    task=ToDos.objects.get(id=task_id)
    task.delete()
    return redirect("/")
    
        
        


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request)