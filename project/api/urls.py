from django.urls import path,include


urlpatterns=[
    path('public/', include('project.api.public.urls')),
]
