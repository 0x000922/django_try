from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader
#from django
# Create your views here.


def customer_forms(request):
    pass

def custom_sql_db_display(request, name):
    '''
    this query can return all the tables in RDBMS_project database
    using raw sql and django connections 
    '''    
    
    with connection.cursor() as cursor:
        sql_statement = "select * from main_{}".format(name)
        try:
            cursor.execute(sql_statement)
            r = list(cursor.fetchall())
            print(cursor.execute("desc main_films"))
        except:
            return HttpResponse("model does not exist")
    template = loader.get_template('main/tables_view.html')
    context = {
        'r': r,
        'name': name,
    }
            
    return HttpResponse(template.render(context,request))
    

def custom_fetch(request, name, id):
    pass


