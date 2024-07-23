from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    template_name = "diagnostic_center/base.html"

class HomeTemplateView(TemplateView):
    template_name = "diagnostic_center/home.html"

class AboutTheClinicTemplateView(TemplateView):
    template_name = "diagnostic_center/about_the_clinic.html"

class DirectionsTemplateView(TemplateView):
    template_name = "diagnostic_center/directions.html"

class ContactsTemplateView(TemplateView):
    template_name = "diagnostic_center/contacts.html"