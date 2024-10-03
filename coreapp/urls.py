from django.urls import path, include

urlpatterns = [
    path('public', include('coreapp.api.urls')),
]
