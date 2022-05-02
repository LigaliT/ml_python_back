# backend/server/apps/endpoints/urls.py file
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", views.EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", views.MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlrequests", views.MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path(r"api/v1/", include(router.urls)),
    path(r"api/v1/<endpoint_name>/predict", views.PredictView.as_view(), name="predict")
]