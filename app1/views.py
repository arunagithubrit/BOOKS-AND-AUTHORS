
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from app1.forms import RegistrationForm,LoginForm
from app1.models import User
# Create your views here.
# library_app/views.py
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import LoginForm
from django.contrib import messages

from app1.models import Author,Book
from app1.forms import AuthorForm,BookForm

class SignInView(SuccessMessageMixin, FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_message = "Login successfully"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)

            if user and user.is_superuser:
                login(request, user)
                messages.success(request, self.success_message)
                return redirect("index")
            else:
                messages.error(request, "Invalid credentials or you are not a superuser.")
                return render(request, self.template_name, {"form": form})
        else:
            messages.error(request, "Invalid form submission.")
            return render(request, self.template_name, {"form": form})


class IndexView(TemplateView):
    template_name="index.html"


class AuthorAddView(CreateView,ListView):
    model=Author
    form_class=AuthorForm
    template_name="addauthor.html"
    success_url=reverse_lazy("author-add")
    context_object_name="authors"

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return redirect("author-add")

    def get_queryset(self):
        return Author.objects.filter(status=False)
    

class BookAddView(CreateView,ListView):
    model=Book
    form_class=BookForm
    template_name="addbook.html"
    success_url=reverse_lazy("book-add")
    context_object_name="books"

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return redirect("book-add")

    def get_queryset(self):
        return Book.objects.filter(status=False)
