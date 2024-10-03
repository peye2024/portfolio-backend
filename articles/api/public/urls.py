from rest_framework.routers import DefaultRouter

from articles.api.public import views

router = DefaultRouter()
router.register(r'article', views.ArticleListView, basename='article')

urlpatterns = [

]

urlpatterns += router.urls
