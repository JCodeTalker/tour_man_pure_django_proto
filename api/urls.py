from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
path('admin/', admin.site.urls),
path("login", views.login_request, name="login"), 
path("logout", views.logout_request, name= "logout"), 
path("register", views.register_request, name="register"), 
path('user_detail',views.user_detail_view, name='user_detail'), 
path('update_profile',views.update_profile, name='update_profile'), 
path('delete_user_view', views.delete_user_view, name='delete_user_view'), 
path('create_deck',views.create_deck), 
path('<int:id>/detail',views.detail_view, name='detail'), 
path('<int:id>/update',views.update_view, name='update'), 
path('<int:id>/delete', views.delete_view, name='delete_view'), 
path('list',views.list_view, name='list'),
path('',views.list_view)
]
