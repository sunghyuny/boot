from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.signup, name='signup'),
    path('agreement/', views.agreement, name='agreement'),
    path('find_id/', views.find_id, name='find_id'),
    path('find_pw/', views.find_pw, name='find_pw'),
]