from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExecuteSQL(APIView):
    def post(self, request, *args, **kwargs):
        try:
            sql_command = request.data.get('sql')
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
            return Response({"result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
