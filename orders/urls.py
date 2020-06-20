from django.urls import path
from .views import CartListView, CartPurchaseView,CartSucessView

app_name='orders'

urlpatterns = [
	path('cart/', CartListView.as_view(), name='cart'),
	path('cart_sucess/', CartSucessView.as_view(), name='cart_sucess'),
	path('cart/purchase/', CartPurchaseView.as_view(), name='cart_purchase')
]