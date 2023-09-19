from django.urls import path
from .views import ListChocolate,DetailChoco,ChocoCheckoutView,CartAPIView
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    # path('api/',views.home,name='home'),
    path('chocolates/',ListChocolate.as_view(),name='list'),
    path('details/<int:pk>/',views.DetailChoco.as_view(),name='details'),
    path('checkout/<int:pk>/',views.ChocoCheckoutView.as_view(),name='checkout'),
    path('cart/',views.CartAPIView.as_view(),name='cart'),


]