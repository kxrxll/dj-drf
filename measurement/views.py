# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer


class SensorView(APIView):
    def post(self, request, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_sensor = Sensor(name=name, description=description)
        new_sensor.save()
        return Response({'status': 'OK'})

    def patch(self, request, **kwargs):
        sensor_id = int(request.POST.get('id'))
        name = request.POST.get('name')
        description = request.POST.get('description')
        sensor = Sensor.objects.get(id=sensor_id)
        sensor.name = name
        sensor.description = description
        sensor.save()
        ser = SensorSerializer(sensor)
        return Response(ser.data)
        # return Response({'status': 'OK'})

    def get(self, request, **kwargs):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)


class MeasurementView(CreateAPIView):
    def post(self, request, **kwargs):
        sensor_id = request.POST.get('id')
        temperature = request.POST.get('temperature')
        new_measurement = Measurement(sensor=sensor_id, temperature=temperature)
        new_measurement.save()
        return Response({'status': 'OK'})
