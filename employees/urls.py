from django.urls import path
from . import views as employee_views


urlpatterns = [
    path('signup/',employee_views.signup,name='signup'),
    path('login/',employee_views.login,name='login'),
    path('updatedetails/',employee_views.updatedetails,name='updatedetails'),
    path('',employee_views.mainpage,name='mainpage'),
    path('showdata/',employee_views.showdata,name='showdata'),
    path('edit/<str:epid>/',employee_views.edit,name='edit'),
    path('delete/<str:epid>/',employee_views.delete,name='delete'),
  

]
