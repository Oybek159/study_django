from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse



urlpatterns = [    # Admin URL
    path('admin/', admin.site.urls),
    path('', include('studyapp.urls'))
]
