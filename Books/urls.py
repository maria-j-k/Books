from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views 


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db/', views.BookWriteView.as_view(), name='db'),
    path('', include(router.urls)),
]
