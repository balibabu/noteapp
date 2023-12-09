from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse
def api_overview(request):
    api_endpoints = {
        "Get Notes List": "/api/notes/",
        "Add Note": "/api/notes/",
        "Get Note Detail": "/api/notes/{id}/",
        "Update Note": "/api/notes/{id}/",
        "Delete Note": "/api/notes/{id}/",
        "POST SQL commands":"/api/sql/"
    }
    return JsonResponse(api_endpoints)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('api/', include('sql.urls')),
    path('',api_overview, name='api-overview')
]
