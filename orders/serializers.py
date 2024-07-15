from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity']



class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity', 'created_at']


class UpdateOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_status']
