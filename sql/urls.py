from django.urls import path
from .views import ExecuteSQL

urlpatterns = [
    path('sql/', ExecuteSQL.as_view(), name='execute_sql'),
]