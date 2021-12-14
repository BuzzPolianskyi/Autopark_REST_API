from django.urls import path, include
from park_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Drivers', views.DriverList)

urlpatterns = [
    path('drivers/driver/', views.DriverList.as_view()),
    path('drivers/driver/<int:pk>/', views.DriverDetail.as_view()),
    path('vehicles/vehicle/', views.VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', views.VehicleDetail.as_view())
]
'''
    path('drivers/', views.DriverList.as_view()),
    path('drivers/', views.DriverList.as_view()),  # GET /drivers/driver/?created_at__gte=10-11-2021
    path('drivers/', views.DriverList.as_view()),  # GET /drivers/driver/?created_at__lte=16-11-2021

    path('drivers/<int:pk>/', views.DriverDetail.as_view()),
    path('drivers/<int:pk>/', views.DriverDetail.as_view()),  # delete
    path('drivers/<int:pk>/', views.DriverDetail.as_view()),  # update
'''