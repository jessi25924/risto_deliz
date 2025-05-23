from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # I’ll add login, dashboard, etc., here later
]