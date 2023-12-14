from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .sqlitedictionary import SQLiteDictDB

sqlDict=SQLiteDictDB()

@api_view(['POST'])
def execute_sql(request):
    try:
        query = request.data
        if query.get('type')=='sql':
            result=perform_sql_command(query.get('command'))
        elif query.get('type')=='sqlitedict':
            result=perform_sqliteDictDB(query)
        else:
            result="invalid request format"
        return Response({"result": result}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

def perform_sql_command(command):
    with connection.cursor() as cursor:
        cursor.execute(command)
        result = cursor.fetchall()
        return result
    
def perform_sqliteDictDB(query):
    sqlDict.set_file('constant')
    action=query.get('action')
    prefix=query.get('prefix',"")

    if action=='get_table_names':
        tables=sqlDict.get_table_names()
        return [table_name for table_name in tables if table_name.startswith(prefix)]
    
    data=query.get('data')
    table=prefix+data.get('table')
    sqlDict.set_table_name(table)

    if action=='get_keys':
        return sqlDict.get_keys()
    if action=='get_content_as_dict':
        return sqlDict.get_content_as_dict()
    if action=='deleteTable':
        sqlDict.deleteTable(table)
    
    key=data.get('key')

    if action=='read':
        return sqlDict.read(key)
    if action=='has':
        return sqlDict.has(key)
    if action=='delete':
        sqlDict.delete(key)
        return 'deleted successfully'
    
    value=data.get('value')

    if action=='override':
        sqlDict.override(key,value)
        return 'data inserted successfully'
    
    return '''actions you can perform: read,has,get_table_names,get_keys,get_content_as_dict,delete,deleteTable'''
