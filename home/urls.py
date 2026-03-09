from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home_page,name='index'),
    path('about/', views.about_page,name='about'),
    path('post/<int:id>/',views.post_details,name='post_details'),
    path('create/',views.create_post,name='create_post'),
    path('update/<int:id>/',views.update_post,name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('search/',views.search,name='search')


]