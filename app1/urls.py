from django.urls import path
from app1.views import SignUpView,SignInView,IndexView


urlpatterns=[
     path("register/",SignUpView.as_view(),name='signup'),
     path('login/',SignInView.as_view(),name='signin'),
     path("index/",IndexView.as_view(),name="index"),

]