from django.urls import path  
from . import views  

app_name = 'accounts'  

urlpatterns = [  
    path('login/', views.login_view, name='login'), 
    path('signup/',views.signup,name='signup'),
    # Add other paths related to authentication here, if needed  
]  