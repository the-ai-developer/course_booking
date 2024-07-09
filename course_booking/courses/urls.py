from django.urls import path
from . import views

urlpatterns = [
    path('course_list', views.course_list, name='course_list'),
    path('', views.home, name='home'),
    path('about-us/',views.aboutus,name='aboutus'),
    path('contact-us/',views.contact,name='contactus'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('course/edit/', views.course_edit, name='course_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
