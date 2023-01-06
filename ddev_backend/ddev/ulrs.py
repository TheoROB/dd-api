from rest_framework import routers
from ddev.views import *

router = routers.DefaultRouter()
router.register('player', PlayerViewSet)
router.register('user', UserViewSet)
router.register('result', ResultViewSet)