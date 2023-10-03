"""
URL configuration for assg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('register/',views.Register.as_view(),name="create"),
    path('login/',views.LoginApi.as_view(),name="create"),
    path('create/',views.create,name='create'),
    path('get/',views.get,name='get'),
    path('partial-update/<int:pk>',views.partial_update,name="partial-update"),
    path('full-update/<int:pk>',views.fully_update,name="partial-update"),
    path('deleted/<int:pk>',views.deleted,name='deleted'),
    path('admin/', admin.site.urls),
]
