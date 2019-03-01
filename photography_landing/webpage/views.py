from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = "webpage/home.html"

class LaPage(TemplateView):
    template_name = "webpage/losangeles.html"

class SeattlePage(TemplateView):
    template_name = "webpage/seattle.html"

class PortlandPage(TemplateView):
    template_name = "webpage/portland.html"

class AboutPage(TemplateView):
    template_name = "webpage/about.html"

class ContactPage(TemplateView):
    template_name = "webpage/contact.html"
