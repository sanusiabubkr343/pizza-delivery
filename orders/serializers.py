from dataclasses import fields
from email.policy import default
from pyexpat import model
from django.forms import modelformset_factory

import orders
from  .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=22)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()
  
    class Meta:
        model = Order
        fields = ['id','size','order_status','quantity']
        # fields ='__all__'
        
class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=22)
    order_status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    
  
    class Meta:
        model = Order
        fields = ['id','size','order_status','quantity','created_at','updated_at']
        # fields = '__all__'
        
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField()

    class Meta:
        model = Order
        fields = ['order_status']
        
        