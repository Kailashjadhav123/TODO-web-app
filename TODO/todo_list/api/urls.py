from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register('todo', views.ListSerializerview , basename='todo')

urlpatterns = [
    path('api/', include(router.urls)) 
]
