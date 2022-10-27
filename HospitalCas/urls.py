"""HospitalCas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from hospitalbackend import views
from django.contrib import admin
from django.urls import path

#es una especie de router (enrutador) que tiene el framework
urlpatterns = [
    #cada vez que llegue una peticion con este patron
    #solomente va el complento (no va la parte del servidor) , segundo parametro en el patron es la vista que va atender el requerimiento
    path('admin/', admin.site.urls),
    #ENDPOINTS Usuario
    path('user/', views.userView.UserListCreateview.as_view()),
    path('user/<int><pk>', views.userView.UserRetriveUpdateDeleteView.as_view()),
    #ENDPOINTS Medico
    path('user/', views.doctorView.DoctorListCreateview.as_view()),
    path('user/<int><pk>', views.doctorView.DoctorRetriveUpdateDeleteView.as_view()),
]
