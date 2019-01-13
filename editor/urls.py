from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

router.register('authors', viewset.AuthorViewset)
router.register('users', viewset.UserViewset)
router.register('drawings', viewset.ViewDrawingViewset)

urlpatterns = router.urls
