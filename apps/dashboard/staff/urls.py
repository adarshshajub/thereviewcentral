from django.urls import path
from apps.dashboard.staff.views import staff_dashboard


urlpatterns = [

    path("", staff_dashboard),
]