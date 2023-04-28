from django.shortcuts import render

from django.http import HttpResponse, HttpResponseForbidden
from django.db import connection

from .sql_middleware import sqlia_detector


def sqlia_all_details(request, id:str):
    cursor = connection.cursor()
    #  query excute
    query = "select name, discription from person where id=%s" % id
    cursor.execute(query)
    rows = cursor.fetchall()
    return HttpResponse(rows)

def blocked_all_details(request, id:str):
    reference_query = "select name, description from person where id= }"
    instance_query = "select name, description from person where id=%s" % id

    if sqlia_detector(reference_query, instance_query, id):
        return HttpResponseForbidden()
    
    return sqlia_all_details(request, id)

def sqlia_details_from_other_table(request, id:str):
    cursor = connection.cursor()
    #  query excute
    query = "select name from person where id=%s" % id
    cursor.execute(query)
    rows = cursor.fetchall()
    return HttpResponse(rows)

def sqlia_city(request, id:str):
    cursor = connection.cursor()
    #  query excute
    query = "select name from city %s" % id
    cursor.execute(query)
    rows = cursor.fetchall()
    return HttpResponse(rows)


