
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
from django.db.models import Q
from django.core.paginator import Paginator
from app1.models import Author,Book
from app1.forms import AuthorForm,BookForm




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"permission denied for current user!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


decs=[signin_required,is_admin]


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
                return redirect("author-add")
            else:
                messages.error(request, "Invalid credentials or you are not a superuser.")
                return render(request, self.template_name, {"form": form})
        else:
            messages.error(request, "Invalid form submission.")
            return render(request, self.template_name, {"form": form})


class IndexView(TemplateView):
    template_name="base.html"

@method_decorator(decs,name="dispatch")
class AuthorAddView(CreateView,ListView):
    model=Author
    form_class=AuthorForm
    template_name="addauthor.html"
    success_url=reverse_lazy("author-add")
    context_object_name="authors"
    # paginate_by = 3

    def form_valid(self, form):
        messages.success(self.request,"author added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"author adding failed")
        return redirect("author-add")

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Author.objects.filter(Q(author_name__icontains=query))
        return Author.objects.all()
        # return Author.objects.filter(status=False)
    
@method_decorator(decs,name="dispatch")
class BookAddView(CreateView,ListView):
    model=Book
    form_class=BookForm
    template_name="addbook.html"
    success_url=reverse_lazy("book-add")
    context_object_name="books"

    def form_valid(self, form):
        messages.success(self.request,"book added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"book adding failed")
        return redirect("book-add")

    def get_queryset(self):
        query = self.request.GET.get('r')
        if query:
            return Book.objects.filter(Q(book_name__icontains=query))
        return Book.objects.all()
        # return Book.objects.filter(status=False)

@signin_required
@is_admin
def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")