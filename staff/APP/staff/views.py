from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    currentdate = datetime.date.today()
    formatdate = currentdate.strftime("%d/%b/%y")
    return render(request, 'home1.html',
                  {'current_date':currentdate,
                    'format_date':formatdate})
    #setup render template current_date  formatedate 
#git extension