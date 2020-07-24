from django.urls import path
from . import views
from .views import IndexView, CustomerFormView

urlpatterns = [
    path('all_table/<name>',views.custom_sql_db_display,name = 'data_display' ),
    path('', IndexView.as_view(),name = 'index'),
    path('all_films', views.all_films, name = 'all_films'),
    path('sbid', views.booking_id_search, name = 'booking_id_search'),
    path('reg', CustomerFormView.as_view(), name = 'reg'),
    
]