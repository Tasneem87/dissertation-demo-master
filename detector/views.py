from django.shortcuts import render

from django.http import HttpResponse
from django.db import connection

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

def sqlia_check(request, id:str):
    # application input
    # SQL query (IA)

    # Step 1 string matching
    # Step 2 radom number


    cursor = connection.cursor()
    #  query excute
    query = "select name, description from person where id=%s" % id
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return HttpResponse(rows)


def sqlia_all_details(request, id:str):
        cursor = connection.cursor()
        #  query excute
        query = "select name, description from person where id=%s" % id
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return HttpResponse(rows)





# two filter and filtering 

