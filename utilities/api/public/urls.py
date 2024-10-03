from rest_framework.routers import DefaultRouter

from utilities.api.public import views

router = DefaultRouter()
router.register('maintainer', views.MaintainerListView)
router.register('contact', views.ContactMessageCreateView)

urlpatterns = [

]

urlpatterns += router.urls
