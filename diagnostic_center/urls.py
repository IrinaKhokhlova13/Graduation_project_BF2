from django.urls import path
from diagnostic_center.apps import DiagnosticCenterConfig
from diagnostic_center.views import BaseTemplateView, HomeTemplateView, AboutTheClinicTemplateView, \
    ContactsTemplateView, DoctorListView, AppointmentListView, ServiceListView, AppointmentCreateView

app_name = DiagnosticCenterConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('about_the_clinic/', AboutTheClinicTemplateView.as_view(), name='about_the_clinic'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('doctor/list/', DoctorListView.as_view(), name='doctor_list'),
    path('appointment/list/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment/new', AppointmentCreateView.as_view(), name='create_appointment'),
    path('service/list/', ServiceListView.as_view(), name='service_list'),
]
