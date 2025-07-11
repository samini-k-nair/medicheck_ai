# from django.urls import path

# from.import views

# urlpatterns = [

#     path('home/',views.HomeView.as_view(),name='home'),

#     path('login/',views.HomeView.as_view(),name='login'),

#     path('symptom_checker/',views.HomeView.as_view(),name='symptom_checker'),

   
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('symptom_checker/', views.Symptom_checkerView.as_view(), name='symptom_checker'),
]
