from django.urls import path, include;
from . import views;
from rest_framework import routers;

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', include(router.urls)),
    path('menu/', views.MenuItemView.as_view(), name="menu-list"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="menu-detail"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]