from django.urls import include, path

from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'wishes', views.WishViewSet)
router.register(r'tickets', views.TicketViewSet)


urlpatterns = [
    path(r'api/whoami', views.CurrentUserView.as_view(), name='current_user'),
    path(r'api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include(router.urls)),
]
