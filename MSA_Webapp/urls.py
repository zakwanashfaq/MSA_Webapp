"""MSA_Webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


import donate.views
import prayerTimes.views
import home.views
import aboutUs.views
import contacts.views
import executives.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('prayertimes/', include('prayerTimes.urls')),
    path('contacts/', include('contacts.urls')),
    path('executives/', include('executives.urls')),
    path('donate/', include('donate.urls')),
    path('aboutus/', include('aboutUs.urls')),
    path('about/', include('aboutUs.urls')),
    path('donate_click', donate.views.donate_home),
    path('about_click', aboutUs.views.about),
    path('contact_click', contacts.views.contact),
    path('executives_click', executives.views.executives),
    path('prayer_click', prayerTimes.views.prayer),
    path('home_click', home.views.index),
]
