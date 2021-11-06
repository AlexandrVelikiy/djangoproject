from django.urls import path

from epra.views import Dashbord

urlpatterns = [
   path('', Dashbord.as_view(), name='dashboard'),
]