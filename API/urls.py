from django.urls import path
from API.views import ParseView

urlpatterns = [
    path('parse', ParseView.as_view())
]