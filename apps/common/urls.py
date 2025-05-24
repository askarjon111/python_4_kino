from django.urls import path

from apps.common.views import home_view


urlpatterns = [
    path('', home_view, name='home'),
]

