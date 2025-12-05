from django.shortcuts import render,HttpResponse,redirect
from .models import Student,User,Teacher
from django.contrib.auth import authenticate,logout,login
# from .models import book,product,event,College,Image,File,Author,Bookk,Login,Ghilna,Trainer
from studentt import settings
from .models import Trainer,Bookss
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView

# Create your views here.
def home(request):
    return render(request,"home.html")

def studentregister(request):
    if request.method=="POST":
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['email']
        a=request.POST['address']
        n=request.POST['number']
        g=request.POST['guardian']
        u=request.POST['username']
        p=request.POST['password']
        new_user=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,address=a,phone_number=n,usertype='student',is_active=False)
        new_user.save()
        x=Student.objects.create(student_id=new_user,guardian=g)
        x.save()
        return HttpResponse("registration successfully")
    else:
        return render(request,"studentregister.html")
    
def teacherregister(request):
    if request.method=="POST":
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['email']
        a=request.POST['address']
        n=request.POST['number']
        s=request.POST['salary']
        e=request.POST['experience']
        u=request.POST['username']
        p=request.POST['password']
        new_user=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,address=a,phone_number=n,usertype='teacher',is_active=True,is_staff=True)
        new_user.save()
        x=Teacher.objects.create(salary=s,experience=e,teacher_id=new_user)
        x.save()
        return HttpResponse("registration successfully")
    else:
        return render(request,"teacherregister.html")
    
def logins(request):
    if request.method=="POST":
          u=request.POST['username']
          p=request.POST['password']
          userpass=authenticate(request,username=u,password=p)
          if  userpass is not None  and userpass.is_superuser==1:
               return redirect('adminhome')
          elif  userpass is not None  and userpass.is_staff==1:
               login(request,userpass)
               request.session['teach_id']=userpass.id
               return redirect("teacherhome")
          elif  userpass is not None  and userpass.is_active==1:
               login(request,userpass)
               request.session['stud_id']=userpass.id
               return redirect("studenthome")
          else:
               return HttpResponse("invalid login")
    else:
         return render(request,'login.html')
          
def teacherhome(request):
    return render(request,'teacherhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def adminhome(request):
    return render(request,"adminhome.html")

def view_student_admin(request):
    x=Student.objects.all()
    return render(request,"view_student.html",{"view":x})

def view_teacher(request):
    x=Teacher.objects.all()
    return render(request,"view_teacher.html",{"data":x})

def logouts(request):
    if "stud_id" in request.session:
        del request.session['stud_id']
    else:
        if "teach_id" in request.session:
            del request.session['teach_id']
            logout(request)
    return redirect("logins")

def approve_student(request,id):
    Stud=Student.objects.select_related("student_id").get(id=id)
    Stud.student_id.is_active=True
    Stud.student_id.save()
    return redirect("view_student_admin")

def view_student_teacher(request):
    x=Student.objects.all()
    return render(request,"view_student_teacher.html",{"view":x})

def delete(request,id):
    stud=Student.objects.get(id=id)
    user_id=stud.student_id.id
    stud.delete()
    user=User.objects.get(id=user_id)
    user.delete()
    return redirect('view_student_admin')

def tdelete(request,id):
    teach=Teacher.objects.get(id=id)
    user_id=teach.teacher_id.id
    teach.delete()
    User.objects.get(id=user_id).delete()
    return redirect('view_teacher')

class Trainercreate(CreateView):
    model=Trainer
    template_name="trainercreate.html"
    fields="__all__"
    success_url="/Trainercreate/"

class Trainerlist(ListView):
     model=Trainer
     template_name="trainerlist.html"
     context_object_name="a"

class Trainerdetail(DetailView):
     model=Trainer
     template_name="trainerdetail.html"
     context_object_name="a"

class Trainerupdate(UpdateView):
     model=Trainer
     template_name="trainercreate.html"
     fields="__all__"
     success_url="/Trainercreate/"

class Trainerdelete(DeleteView):
    model=Trainer
    template_name="trainerdelete.html"
    success_url="/Trainercreate/"

def book_create_view(request):
    view=CreateView.as_view(
        model=Bookss,
        template_name="book_form.html",
        fields="__all__",
        success_url="/Bookss/"
    )
    return view(request)

def book_list_view(request):
    view=ListView.as_view(
        model=Bookss,
        template_name="book_list.html",
        context_object_name="b"
    )
    return view(request)

def book_detail_view(request,pk):
    view=DetailView.as_view(
        model=Bookss,
        template_name="book_detail.html",
        context_object_name="b"
    )
    return view(request,pk=pk)

def book_update_view(request,pk):
    view=UpdateView.as_view(
        model=Bookss,
        template_name="book_form.html",
        fields="__all__",
        success_url="/Bookss/"
    )
    return view(request,pk=pk)

def book_delete_view(request,pk):
    view=DeleteView.as_view(
        model=Bookss,
        template_name="book_delete.html",
        success_url="/Bookss/"
    )
    return view(request,pk=pk)


def view_student(request):
    x=Student.objects.all()
    return render(request,"view_student_teacher.html",{"view":x})

def editteacher(request):
   teach=request.session.get('teach_id')

   teacher=Teacher.objects.get(teacher_id=teach)
   user=User.objects.get(id=teach)


   return render(request,"editteacher.html",{"view": teacher,"data":user})

def updateteacher(request,id):
    if request.method == "POST":
         teach=Teacher.objects.get(id=id)
         uid=teach.teacher_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         teach.salary=request.POST["salary"] 
         teach.experience=request.POST["experience"] 

         user.save()
         teach.save()

         return redirect(view_teacher)
    
def  editstudent(request):
    stud=request.session.get('stud_id')

    student=Student.objects.get(student_id_id=stud)
    user=User.objects.get(id=stud)


    return render(request,"editstudent.html",{"view": student,"data":user})


def updatestudent(request,id):


    if request.method == "POST":
         stud=Student.objects.get(id=id)
         uid=stud.student_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         stud.guardian=request.POST["guardian"] 
         user.save()
         stud.save()

         return redirect(view_student)
    
def index(request):
    return render(request,"index.html")