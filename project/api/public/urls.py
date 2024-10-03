from rest_framework.routers import DefaultRouter

from project.api.public import views

router = DefaultRouter()
router.register(r'tag', views.TagListView, basename='tag')
router.register(r'project', views.ProjectListView, basename='project')

urlpatterns = [

]

urlpatterns += router.urls
