from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import book_table

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registrations/logged_out.html'), name='logout'),
    path('book/', views.book_table, name='book_table'),
    path('booking/<int:pk>/edit/', views.edit_booking, name='edit_booking'),
    path('booking/<int:pk>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('menu/', views.menu, name='menu'),
]