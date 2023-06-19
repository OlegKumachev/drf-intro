

from .models import Sensor, Measurement
from .serializers import SensorDetailsSerializer, SensorsSerialaizer, MeasurementSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, CreateAPIView


class SensorCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerialaizer


class MeasurementUpdateAPIView(ListCreateAPIView):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer
