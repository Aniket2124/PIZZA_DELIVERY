from django.shortcuts import render, get_object_or_404
from .serializers import OrderSerializer, OrderDetailSerializer, UpdateOrderStatusSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


class OrderCreateListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data=request.data
        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class OrderDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer

    def get(self,request,id):
        order = get_object_or_404(Order, pk=id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        data=request.data
        user = request.user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(customer = user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        order = get_object_or_404(Order, pk=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UpdateOrderStatus(UpdateAPIView):
    serializer_class = UpdateOrderStatusSerializer

    def put(self, request, id):
        order = get_object_or_404(Order, pk=id)
        data = request.data
        serializer = self.serializer_class(data=data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserOrderView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

    def get(self,request,id):
        user = User.objects.get(pk=id)  #To fetch perticular users orders
        orders = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class UpdateUserOrderView(UpdateAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'

    def get(self,request,user_id,id):
        user = get_object_or_404(User, pk=user_id)
        orders = Order.objects.all().filter(customer=user).get(pk=id)
        serializer = self.serializer_class(instance=orders)
        return Response(data=serializer.data, status=status.HTTP_200_OK)