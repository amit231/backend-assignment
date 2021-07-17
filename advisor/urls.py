
from django.urls import path
from .views import AdvisorAPIView
# print(AdvisorAPIView)
urlpatterns = [
    path('', AdvisorAPIView.as_view()),
]
