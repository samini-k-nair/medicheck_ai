"""
URL configuration for medicheck_ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include

# from django.conf import settings

# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('symptom_scan/',include('symptom_scan.urls')),

    path('authentication/',include('authentication.urls')),

    path('symptom_check/', include('symptom_check.urls')), 

    path('appointments/', include('appointments.urls')),

    path('reports/', include(('reports.urls', 'reports'), namespace='reports')),

    
    path('risk/', include('risk_assessment.urls', namespace='risk_assessment')),

    path('doctor/', include(('doctor.urls', 'doctor'), namespace='doctor')),
]



   

