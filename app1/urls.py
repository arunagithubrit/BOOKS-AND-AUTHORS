from django.urls import path
from app1.views import SignInView,IndexView,AuthorAddView,BookAddView,sign_out_view,AuthorDetailView,total_authors,total_books


urlpatterns=[
     # path("register/",AdminSignupView.as_view(),name='signup'),
     path('login/',SignInView.as_view(),name='signin'),
     path("index/",IndexView.as_view(),name="index"),
     path("author/add/",AuthorAddView.as_view(),name="author-add"),
     path("book/add/",BookAddView.as_view(),name="book-add"),
     path("author/<int:pk>/books/",AuthorDetailView.as_view(),name="author-detail"),
     path("logout/",sign_out_view,name="logout"),
     path("total_authors/",total_authors,name="total-author"),
     path("total_books/",total_books,name="total-books"),






    



]