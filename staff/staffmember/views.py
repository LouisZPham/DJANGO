from django.shortcuts import render
from staffmember.models import Staff  
import datetime
# Create your views here.

def staffinfo(request):
    staf = Staff.objects.all()
    print('myoutput', staf)
    return render(request, 'staff/staffdetails.html', {'sta': staf})
def home(request):
    currentdate = datetime.date.today()
    formatdate = currentdate.strftime("%d/%b/%y")
    return render(request, 'home.html',
                  {'current_date':currentdate,
                    'format_date':formatdate}  )
