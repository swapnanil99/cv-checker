from django.urls import path
from .views import rematch_cv

urlpatterns = [
    path("", rematch_cv, name="rematch_cv"),
]
