from rest_framework.routers import DefaultRouter
from task.views import TaskViewSet
from tile.views import TileViewSet


router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')
router.register('tile', TileViewSet, basename='tile')
urlpatterns = router.urls

