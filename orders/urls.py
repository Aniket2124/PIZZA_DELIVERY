from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order_list'),
    path('details/<int:id>/', views.OrderDetailsView.as_view(), name='update'),
    path('status/<int:id>/', views.UpdateOrderStatus.as_view(), name='status_update'),
    path('user/<int:id>/view_orders/', views.UserOrderView.as_view(), name='order_list_view'),
    path('user/<int:user_id>/view_orders/<int:id>/', views.UpdateUserOrderView.as_view(), name='order_list_view'),
]