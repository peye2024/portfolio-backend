from django.urls import path,include


urlpatterns=[
    path('public/', include('utilities.api.public.urls')),
]
