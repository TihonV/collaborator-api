from rest_framework import routers

from . import viewset

router = routers.SimpleRouter()

router.register('users', viewset.AuthorViewset)
router.register('tags', viewset.TagViewset)
router.register('drawings', viewset.ViewDrawingViewset)
router.register('editors', viewset.EditDrawingViewset)

urlpatterns = router.urls
