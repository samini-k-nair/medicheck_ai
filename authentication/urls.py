# from django.urls import path

# from . import views


# urlpatterns = [

#     path('login/',views.LoginView.as_view(),name='login'),

#     path('register/', register_view, name='register'), 

#     # path('logout/',views.LogoutView.as_view(),name='logout'),

#     # path('register-choices/',views.RegisterChoicesView.as_view(),name='register-choices')

# ]



from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  # ✅ Add this
]
