from django.urls import path
from . import views

app_name = 'web_application'
urlpatterns = [
    path('LA/',views.LaPage.as_view(),name='losangeles'),
    path('seattle/',views.SeattlePage.as_view(),name='seattle'),
    path('portland/',views.PortlandPage.as_view(),name='portland'),
    path('about/',views.AboutPage.as_view(),name='about'),
    path('contact/',views.ContactPage.as_view(),name='contact')
]
