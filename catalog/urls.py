from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_profile',views.addprofile,name ='add_profile'),
    path('saveprofile',views.saveprofile,name ='saveprofile'),
    path('editprofile',views.editprofile,name ='editprofile'),
    path('updateprofile',views.updateprofile,name ='updateprofile'),
    path('profile/', views.profile, name='profile'),
    
    path('book-detail/<int:id>',views.bookdetails,name='bookdetails'),
    
    path('borrow-book/<uuid:book_instance_id>/', views.borrow_book, name='borrow-book'),
    

    # Check the 'name' parameter
    # Other URL patterns...
]

