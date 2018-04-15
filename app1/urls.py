from django.urls import path

from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.log_in, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register, name='register'),
    path('dashboard/create',views.create,name='create'),
    path('dashboard/edit/<int:id>',views.edit,name='edit'),
    path('dashboard/delete/<int:id>',views.delete,name='delete'),
]