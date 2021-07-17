from rest_framework import serializers
from .models import User, Booking


class UserSeializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookingSeializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
