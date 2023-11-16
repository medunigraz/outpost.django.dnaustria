from django.conf.urls import url

from . import views

app_name = "dnaustria"

urlpatterns = [
    url("$", views.DataView.as_view(), name="data"),
]
