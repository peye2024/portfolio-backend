from django.urls import path, include

app_name = 'api-v1'

urlpatterns = [
    path('core/', include('coreapp.api.urls')),
    # path('article/', include('articles.api.urls')),
    path('projects/', include('project.api.urls')),
    path('utilities/', include('utilities.api.urls')),

]
