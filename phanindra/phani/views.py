from django.shortcuts import render
from django.http import HttpRequest
from phani import forms
from phani.forms import NewUserForm,UserForm,UserProfileInfoForm
from phani.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
     context_dict = {'text': 'hello world','number':100}
     return render(request,'phani/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse("you are logged in , Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))






def register(request):

     registered = False

     if request.method == 'POST':
         user_form = UserForm(data=request.POST)
         profile_form = UserProfileInfoForm(data=request.POST)

         if user_form.is_valid() and profile_form.is_valid():

             user = user_form.save()
             user.set_password(user.password)
             user.save()

             profile = profile_form.save(commit=False)
             profile.user = user

             if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
                    profile.save()

                    registered = True
             else:
                    print(user_form.errors,profile_form.errors)
     else:
         user_form = UserForm()
         profile_form = UserProfileInfoForm()
        
     return render(request,'phani/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

    
def other(request):
     return render(request,'phani/other.html')

def form_name(request):
    form = forms.FormName()


    # this is to print the values to console entered in .html page
    if request.method == 'POST':
       form = forms.FormName(request.POST)
       



       if form.is_valid():
            # do something

            print("validation success")
            print("name:"+form.cleaned_data['name'])
            print("email:"+form.cleaned_data['email'])
            print("text:"+form.cleaned_data['text']) 


    return render(request,'phani/formpage.html',{'forms':form})



def User(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error from invalid")

    return render(request,'phani/users.html',{'form':form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("account not active")
        else:
            print("someone tried to login failed")
            print("username:{} and password{}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'phani/login.html',{})

