from django.urls import path

from . import views
from .views import (
    productDetail,
    shop,
    home,
    CategoryView,
    add_to_cart,
    CartView,
    checkoutView

)

urlpatterns = [
    # path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('privacy/', views.privacyPolicy, name="privacyPolicy"),
    path('payment-process/', views.paymentProcess, name="paymentProcess"),
    # path('checkout/', views.checkout, name="checkout"),
    path('refund-returns-policy/', views.terms, name="refundReturnsPolicy"),
    path('order-track/', views.orderTrack, name="orderTrack"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('cart/', views.cart, name="cart"),
    path('become-seller/', views.becomeSeller, name="becomeSeller"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('create-user/', views.createUser, name="createUser"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('change-password/', views.changePassword, name="changePassword"),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('updateProfile/', views.updateProfile, name="updateProfile"),
    path('userorder/', views.userOrder, name="userOrder"),
    path('balance/', views.balance, name="balance"),
    path('chat/', views.chat, name="chat"),
    # path('shop/', views.shop, name="shop"),
    # path('product/', views.productDetail, name="productDetail"),
    path('shop/', shop.as_view(), name='shop'),
    path('product/<slug>/', productDetail.as_view(), name='productDetail'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', checkoutView.as_view(), name='checkout'),
    path('', home.as_view(), name='home'),

]
