from django.urls import path
from diagnostic_center.apps import DiagnosticCenterConfig
from diagnostic_center.views import BaseTemplateView, HomeTemplateView, AboutTheClinicTemplateView, \
    DirectionsTemplateView, ContactsTemplateView

app_name = DiagnosticCenterConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('about_the_clinic/', AboutTheClinicTemplateView.as_view(), name='about_the_clinic'),
    path('directions/', DirectionsTemplateView.as_view(), name='directions'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]
