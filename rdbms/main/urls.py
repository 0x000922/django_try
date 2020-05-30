from django.urls import path
from . import views


urlpatterns = [
    path('all_table/<name>',views.custom_sql_db_display,name = 'data_display' )
    path('all_table')
]