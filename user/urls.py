
from django.urls import path
from .views import UserLoginAPIView, UserRegisterAPIView, AdvisorListAPIView, AdvisorBookingAPIView, BookingListAPIView
# print(AdvisorAPIView)
urlpatterns = [
    path('<int:pk>/advisor/<int:sk>/', AdvisorBookingAPIView.as_view()),
    path('<int:pk>/advisor/booking/', BookingListAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('<int:pk>/advisor/', AdvisorListAPIView.as_view()),
]
