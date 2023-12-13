from django.urls import path
from . import views

urlpatterns = [
    path('sql/', views.execute_sql, name='execute_sql'),
]