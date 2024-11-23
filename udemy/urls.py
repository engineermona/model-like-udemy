from django.urls import path
from .import views
app_name='udemy'
urlpatterns = [path('',views.home,name='home'),]