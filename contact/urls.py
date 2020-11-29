from . import views
from django.urls import path,include

app_name="contact" # you shold write this for url linking  and 'job' is the name of the pp name 

urlpatterns = [
    path("",views.send_message,name="contact"),
]
