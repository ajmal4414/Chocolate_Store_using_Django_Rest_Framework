from django.urls import path
# from .api import RegisterApi
from .views import RegisterView, LoginView

urlpatterns=[
    # path('api/register', RegisterApi.as_view()),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login')

]