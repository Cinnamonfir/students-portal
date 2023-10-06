
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name=''),
    path('delete/<int:pk>', views.delete_student, name='delete'),
    path('add/', views.add, name='add'),


]