from django.shortcuts import render
from APP.staffmember.models import Staff
import datetime
# Create your views here.

def staffinfo(request):
    staf = Staff.objects.all()
    print('myoutput', staf)
    #setup debug phan nay, Json -> chưa hiển thị được.
    return render(request, 'staff/staffdetails.html', {'sta': staf})
def home(request):
    currentdate = datetime.date.today()
    formatdate = currentdate.strftime("%d/%b/%y")
    return render(request, 'home.html',
                  {'current_date':currentdate,
                    'format_date':formatdate})
    #setup render template current_date  formatedate 
#viet Get data.
#tao 1 class home. Truyen nhung bien nhu ftdate ctdate de ke thua.
#class home get.c'mon data. [get_context_data]
##get_context_data get view_teample 
#return html

###get_context_data:
###context['current_date']=hghghg

#models - urls match data - database cung ten.