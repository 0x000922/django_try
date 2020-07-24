from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import Films, Bookings, Customers
from .forms import Booking_id, CustomerForm
from django.views import View
#from django
# Create your views here.

"""
    function view start
"""



def custom_sql_db_display(request, name):
    '''
    this query can return all the tables in RDBMS_project database
    using raw sql and django connections 
    DONOT USE THIS JUST FOR DEMONSTRATION 
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
    

def all_films(request):
    return custom_sql_db_display(request, "films")




"""
function view end
"""
"""
class based view
"""
class IndexView(View):
    def get(self,request):
        return render(request, 'main/indexpage.html')

class CustomerFormView(View):
    form_class = CustomerForm
    template_name = 'main/customerform.html'

    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            a = form.cleaned_data['first_name']
            b = form.cleaned_data['last_name']
            c = form.cleaned_data['email']
            o = Customers(first_name = a, last_name = b, email = c)
            o.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})

class BookingIDSearchView(View):
    form_class = Booking_id
    template_name = 'main/bookingidForm.html'
    sub = False
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'main/bookingidForm.html', {'form' : form, 'submit': self.sub})

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        if request.method == 'POST':
            form = Booking_id(request.POST)
            self.sub = True
            if form.is_valid():
                r = form.cleaned_data['Booking_id']
                book = Bookings.objects.get(id = r)
                reseverd = book.reserved_seat_set.all()
                customer = book.customers
                context = {
                        'customer' : customer,
                        'seats': reseverd,
                        'submit': self.sub,
                        'book': book
                    }
        return render(request, 'main/bookingidForm.html',context)
