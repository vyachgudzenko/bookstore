from django.urls import path
from .views import OrdersPageView,charge

app_name = 'orders'
urlpatterns = [
    path('', OrdersPageView.as_view(),name='orders'),
    path('charge/', charge, name='charge'),
]
