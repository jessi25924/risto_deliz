from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # I’ll add login, dashboard, etc., here later
]