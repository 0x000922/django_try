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
def index(request):
    template = loader.get_template('main/indexpage.html')
    context = {}
    return HttpResponse(template.render(context,request))


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
    

def all_films(request):
    return custom_sql_db_display(request, "films")


def booking_id_search(request):
    sub = False
    if request.method == 'POST':
        form = Booking_id(request.POST)
        sub = True
        if form.is_valid():
            r = form.cleaned_data['Booking_id']
            book = Bookings.objects.get(id = r)
            reseverd = book.reserved_seat_set.all()
            customer = book.customers
            '''
            sql = "select * from main_reserved_seat as c, main_bookings as b where c.booking_id = b.id and b.id={}".format(r.id)
            with connection.cursor() as cur:
                try:
                    cur.execute(sql)
                    r = list(cur.fetchall())
                except:
                    return HttpResponse("model does not exist")
            '''
            context = {
                'customer' : customer,
                'seats': reseverd,
                'submit': sub,
                'book': book
            }
            return HttpResponse(render(request,'main/bookingidForm.html', context ))
    
    else:
        form = Booking_id()
    
    return render(request, 'main/bookingidForm.html', {'form' : form, 'submit': sub})
    
def customerform(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['first_name']
            b = form.cleaned_data['last_name']
            c = form.cleaned_data['email']
            o = Customers(first_name = a, last_name = b, email = c)
            o.save()
            return HttpResponseRedirect('/')
        
    else:
        form = CustomerForm()
    return render(request, 'main/customerform.html', {'form': form})

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

    def get(self,request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            a = form.cleaned_data['first_name']
            b = form.cleaned_data['last_name']
            c = form.cleaned_data['email']
            o = Customers(first_name = a, last_name = b, email = c)
            o.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})