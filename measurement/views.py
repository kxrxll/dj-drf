from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorCreateSerializer, MeasurementCreateSerializer, \
    MeasurementSerializer


class SensorView(APIView):
    def post(self, request, **kwargs):
        ser = SensorCreateSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response({'status': 'OK'})

    def patch(self, request, **kwargs):
        sensor_id = int(request.POST.get('id'))
        name = request.POST.get('name')
        description = request.POST.get('description')
        sensor = Sensor.objects.get(id=sensor_id)
        sensor.name = name
        sensor.description = description
        sensor.save()
        ser = SensorCreateSerializer(sensor)
        return Response(ser.data)

    def get(self, request, **kwargs):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)


class MeasurementView(APIView):
    def post(self, request, **kwargs):
        ser = MeasurementCreateSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'status': 'OK'})
        return Response({'status': 'ERROR'})

    def get(self, request, measurement_id):
        sensors = Measurement.objects.get(id=measurement_id)
        ser = MeasurementSerializer(sensors, many=True)
        return Response(ser.data)
