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
    prefix=query.get('prefix')
    action=query.get('action')
    data=query.get('data')
    table=data.get('table')
    sqlDict.set_file(prefix)
    sqlDict.set_table_name(table)
    
    if action=='insert':
        key=data.get('key')
        value=data.get('value')
        sqlDict.override(key,value)
    elif action=='read':
        key=data.get('key')
        return sqlDict.read(key)
    elif action=='has':
        key=data.get('key')
        return sqlDict.has(key)
    elif action=='get_table_names':
        return sqlDict.get_table_names()
    elif action=='get_keys':
        return sqlDict.get_keys()
    elif action=='get_content_as_dict':
        return sqlDict.get_content_as_dict()
    elif action=='delete':
        key=data.get('key')
        sqlDict.delete(key)
    elif action=='deleteTable':
        sqlDict.deleteTable(table)
    else:
        return '''actions you can perform: read,has,get_table_names,get_keys,get_content_as_dict,delete,deleteTable'''
    return 'done'
