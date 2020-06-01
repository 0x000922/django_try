from django.urls import path
from . import views


urlpatterns = [
    path('all_table/<name>',views.custom_sql_db_display,name = 'data_display' ),
    path('', views.index, name = 'index'),
    path('all_films', views.all_films, name = 'all_films'),
    path('sbid', views.booking_id_search, name = 'booking_id_search'),
    path('reg', views.customerform, name = 'reg'),
    
]