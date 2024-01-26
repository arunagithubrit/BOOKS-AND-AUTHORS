
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from app1.forms import RegistrationForm,LoginForm
from app1.models import User
# Create your views here.
class SignUpView(CreateView):

    template_name="register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})
            


class IndexView(TemplateView):
    template_name="index.html"