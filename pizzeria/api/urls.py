from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuItemViewSet)
router.register(r'cart', views.OrderLineViewSet)
router.register(r'cart-text', views.CartViewSet)
router.register(r'toppings', views.ToppingsViewSet)
router.register(r'order', views.OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
