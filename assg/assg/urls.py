from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
    

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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
