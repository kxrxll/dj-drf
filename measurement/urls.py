from django.urls import path

from measurement.views import SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<measurement_id>/', MeasurementView.as_view())
]

