from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("authors",views.AuthorListView,basename='authors')
router.register("books",views.BookListView,basename='books')

urlpatterns=[

    
]+router.urls