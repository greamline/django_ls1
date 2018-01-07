"""hr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from analitics import views as analitic_views
from corp import views as corp_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', analitic_views.main),
    url(r'^corp/$', corp_views.CorpsListView.as_view()),
    url(r'^c/$', corp_views.get_corp),
    url(r'^m/$', analitic_views.MetricsListView.as_view()),
    url(r'^submit_metrics/', analitic_views.SubmitMetrics.as_view()),
    # path('reg/', include('reg.urls')),
    path('auth/', include('authapp.urls', namespace = 'authapp')),
]
