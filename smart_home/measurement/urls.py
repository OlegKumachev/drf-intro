from django.urls import path

from .views import *


urlpatterns = [
    path('sensors/', SensorCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateAPIView.as_view()),
    path('measurements/', MeasurementUpdateAPIView.as_view()),

]
