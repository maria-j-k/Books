from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views 


router = routers.DefaultRouter()
router.register(r'', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db/', views.BookWriteView.as_view(), name='db'),
    path('books/', include(router.urls)),
    path('openapi', get_schema_view(
        title="Books REST API",
        description="API",
        version="1.0.0"
    ), name='openapi-schema'),
]



