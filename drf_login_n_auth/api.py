from rest_framework import routers
from rental import views


router = routers.DefaultRouter()
router.register(r'friends', views.FriendViewSet)
router.register(r'belongings', views.BelongingViewSet)
router.register(r'borrowings', views.BorrowedViewSet)