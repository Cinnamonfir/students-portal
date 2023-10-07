
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name=''),
    path('delete/<int:pk>', views.delete_student, name='delete'),
    path('add', views.add, name='add'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login')


]