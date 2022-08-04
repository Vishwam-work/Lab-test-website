from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.urls import is_valid_path
from mypro import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .form import Sampleinput
from . tokens import generate_token

from django.views.decorators.csrf import csrf_exempt
# from myapp.models import Sampletest

# Create your views here.
def index(request):
    return render(request,'index.html')
def health(request):
    return render(request,'health.html')
def contact(request):
    return render(request,'contact.html')

def client(request):
    return render(request,'client.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        lastname=request.POST['lastname']
        email=request.POST['email']
        firstname=request.POST['firstname']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']


    # Validation-----
        if User.objects.filter(username=username):
            messages.error(request,"Username alreay exit please try again")
            return redirect('index')
        if User.objects.filter(email=email).exists():
            messages.error(request,"email already exist ")
            return redirect('index')
        if len(username)>10:
            messages.error(request,"Invalid username")
        if password != confirmpassword:
            messages.error(request,"Invalid Password , Please check!!")
     

        # creating the  email template

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.is_actve=False
        myuser.save()


        subject = "Welcome to H20 lab email Confirmation!! "
        message="Hello "+ myuser.first_name+"!! \n"+"Welcome to H20 lab \n"+"Thank you for visting in our website \n"+"We send a confirmation link so please click on link to activate your account \n"+"Thank you"
        from_email = settings.EMAIL_HOST_USER
        to_list=[myuser,email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

       
        

        # Email link genrate 
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')

        
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(username=username,password=password)

        if(user is not None):
            login(request,user)
            firstname=user.first_name
            return render(request,"index.html",{'firstname':firstname})    
        else:
            messages.error(request," incorrect credentials")
            # redirect('index')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('index')

    
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')



# -------------------------------------------------------

def choice(request):
    return render(request,'choice.html')

def choice1(request):
    return render(request,'choice1.html')

# @csrf_exempt
@login_required(login_url="signin")
def sample(request):
    if request.method == 'POST':
        form = Sampleinput(request.POST)
        if form.is_valid():
            try:
               
                form.save()
                return redirect('/')
            except:
                pass
        else:
            pass
    else:
        form = Sampleinput()
    return render(request, 'sample.html', {'form': form})