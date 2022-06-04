from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name="loginpage"),
    path('signup/', views.signup, name="signup"),
    path('verify/<str:code>', views.verify_code, name="verify"),
    path('sponsors/', views.sponsors, name="sponsors"),
    path('<str:username>', views.influencers, name="influencers")
]
