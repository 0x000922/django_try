from django.contrib import admin
from .models import Films as Film ,Customers as customer,Reserved_seat as seats_reserved, Screenings as screening  
# Register your models here.
admin.site.register(Film)
admin.site.register(customer)
admin.site.register(seats_reserved)
admin.site.register(screening)