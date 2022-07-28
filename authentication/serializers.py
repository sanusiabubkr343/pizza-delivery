from dataclasses import fields
from operator import imod
from pyexpat import model

import phonenumbers
from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username =serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phoneNumber = PhoneNumberField( allow_null = False,allow_blank =False)
    password  = serializers.CharField(min_length = 8,write_only=True)
    
    
    class Meta:
        model= User
        fields =['username','email','phoneNumber','password']
    
    
    
    def validate(self,attrs):
        username_exists =User.objects.filter(username=attrs['username']).exists()
        
        if username_exists:
            raise serializers.ValidationError("User with username exists")
        
        email_exists =User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise serializers.ValidationError("User with email exists")
        
        phone_Number_exists =User.objects.filter(phoneNumber=attrs['phoneNumber']).exists()
        
        if phone_Number_exists:
            raise serializers.ValidationError("User with phoneNumber exists")
        
        
        return super().validate(attrs)
    
    
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email=validated_data['email'],
            phoneNumber = validated_data['phoneNumber']
        )
            
        user.set_password(validated_data['password'])      
        
        user.save()
        
        return user
            