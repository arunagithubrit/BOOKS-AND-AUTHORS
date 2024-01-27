from django.urls import path
from app1.views import SignInView,IndexView,AuthorAddView,BookAddView,sign_out_view


urlpatterns=[
     # path("register/",AdminSignupView.as_view(),name='signup'),
     path('login/',SignInView.as_view(),name='signin'),
     path("index/",IndexView.as_view(),name="index"),
     path("author/add/",AuthorAddView.as_view(),name="author-add"),
     path("book/add/",BookAddView.as_view(),name="book-add"),
     path("logout/",sign_out_view,name="logout"),



    



]