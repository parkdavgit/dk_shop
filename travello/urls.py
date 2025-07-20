from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/<int:user_id>/', views.payment, name='payment'),

    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('detail/<int:dest_id>/', views.detail, name='detail'),
    path('cart/<int:destination_id>/', views.cart, name='cart'),
    path('cartview/<int:user_id>/', views.cartview, name='cartview'),
    path('cartview/<int:user_id>/delete', views.delete_cart, name='delete_cart'),
    path('checkout/<int:user_id>/', views.checkout, name='checkout'),
    path('order/<int:user_pk>/delete', views.delete_order, name='delete_order'),
    path('food_search/', views.food_search, name='food_search'),

    path('food_create/', views.food_create, name='food_create'),
    path('food_edit/<int:destination_id>/', views.food_edit, name='food_edit'),
    path('food_delete/<int:destination_id>/', views.food_delete, name='food_delete'),


    
]