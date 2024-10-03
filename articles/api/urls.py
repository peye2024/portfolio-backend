from django.urls import path, include

urlpatterns = [
    path('public/', include('articles.api.public.urls')),
]
