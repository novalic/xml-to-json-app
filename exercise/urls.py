from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from xml_converter import views, api

router = DefaultRouter()
router.register('converter', api.ConverterViewSet, basename='converter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connected/', views.upload_page, name='upload-file'),
    path('api/', include(router.urls)),
]
