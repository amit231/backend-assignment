from datetime import datetime, timedelta
import jwt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSeializer, BookingSeializer
from .models import User, Booking
from advisor.models import Advisor
from advisor.serializers import AdvisorSerializer

# Create your views here.


class UserRegisterAPIView(APIView):
    def post(slef, request):
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        if(email == '' or password == '' or name == ''):
            print('1 get bad')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        duplicateUser = User.objects.filter(email=email).first()
        # if duplicateUser is None:
        serializer = UserSeializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(email=email)
            jwtToken = jwt.encode({
                'id': user.id,
                'exp': datetime.utcnow() + timedelta(minutes=30),
            }, 'Nurturelabs')
            return Response({'JWT Authentication Token': jwtToken, 'User id': user.id}, status=status.HTTP_200_OK)
        print('2 get bad')
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        if(email != '' and password != ''):
            user = User.objects.get(email=email)
            # print(user.password, password)
            if(user.password == password):
                jwtToken = jwt.encode({
                    'id': user.id,
                    'exp': datetime.utcnow() + timedelta(minutes=30),
                }, 'Nurturelabs')
                return Response({'JWT Authentication Token': jwtToken, 'User id': user.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AdvisorListAPIView(APIView):
    def get(self, request, pk):
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors, many=True)
        return Response(serializer.data)


class BookingListAPIView(APIView):
    def get(self, request, pk):
        allBookings = Booking.objects.all()

        arr = []

        for booking in allBookings:
            print(booking.advisor_id.id, pk)
            if(pk == booking.user_id.id):
                single_booking = {
                    "Advisor_name": booking.advisor_id.name,
                    "Advisor_Profile_pic": booking.advisor_id.photo,
                    "Advisor_id": booking.advisor_id.id,
                    "Booking_time": booking.booking_time,
                    "Booking_id": booking.id,
                }
                arr.append(single_booking)
        print(arr)
        serializer = BookingSeializer(arr, many=True)
        return Response(arr, status=status.HTTP_200_OK)


class AdvisorBookingAPIView(APIView):
    def post(self, request, pk, sk, format=None):
        advisor = Advisor.objects.get(id=sk)
        user = User.objects.get(id=pk)
        booking_time = request.data['Booking_time']
        print(booking_time)
        if(user is not None and advisor is not None):
            d = {
                "advisor_id": sk,
                "user_id": pk,
                "booking_time": booking_time,
            }
            serializer = BookingSeializer(data=d)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                print('hellllllllllllo')
        else:
            print('user,advisor is not there')
        return Response(status=status.HTTP_400_BAD_REQUEST)
