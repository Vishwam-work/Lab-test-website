from django.shortcuts import render,redirect

from adminapp.admin_signup import Adminsignup

from adminapp.models import Admin_signup
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Sample
from myapp.form import Sampleinput

# Create your views here.
@csrf_exempt
def admin_signin(request):
    if request.method == 'POST':

        password = request.POST.get('password')
        username = request.POST.get('username')
        user = Admin_signup.objects.filter(password=password, username=username).count()
        print("____", user)

        if user == 1:
            user = Admin_signup.objects.filter(password=password, username=username)
            for l1 in user:
                request.session['username'] = l1.username
                request.session['id'] = l1.id
                print(l1.username)
                request.session['id'] = l1.id
                return redirect('/table/')
        else:
            messages.error(request, 'Invalid username and password')
        return render(request, 'admin_signin.html')
    else:
        return render(request, 'admin_signin.html')


        
       

def admin_signup(request):
    if request.method=="POST":
        form=Adminsignup(request.POST)
        try:
            form.save()
            return redirect('/admin_signin')
        except:
            pass

    else:
        form=Adminsignup()
        context={'form':form}
        return render(request,'admin_signup.html',context)
def table(request):
    form = Sample.objects.all()
    return render(request,"table.html",{'form':form})
def user(request):
    return render(request,"user.html")
def test(request,id):
    sam = Sample.objects.filter(id=id)
    
    return render(request,"test.html",{'sam':sam})