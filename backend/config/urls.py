from django.urls import path
from api.views import home, about, projects, contact

urlpatterns = [
    path('api/home/', home),
    path('api/about/', about),
    path('api/projects/', projects),
    path('api/contact/', contact),
]