from django.shortcuts import render, redirect
from APP.staffmember.models import Staff
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
import zoneinfo
import datetime

# Create your views here.           

def staffinfo(request):
    staf = Staff.objects.all()
    testtext = 'Testing'
    print('myoutput', staf)
    currentdate = datetime.date.today()
    formatdate = currentdate.strftime("%d/%b/%y")
    return render(request, 'staff/staffdetails.html', {'sta': staf,
                                                       'current_date':currentdate,
                                                    'format_date':formatdate,
                                                    'test_text': testtext})

def home(request):
    currentdate = datetime.date.today()
    formatdate = currentdate.strftime("%d/%b/%y")
    return render(request, 'home.html',
                  {'current_date':currentdate,
                    'format_date':formatdate})
    
x = timezone.now()

def time(request):
    return render(request,'home.html',{'my_date': x})




class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
common_timezones = {
    'London': 'Europe/London',
    'New York': 'America/New_York',
    'Vietnam': 'Vietnam',
}

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'timezone.html', {'timezones': common_timezones})
#hoc debug lai ve check xem co vao function nay hay chua.
    
    
    
    
    #setup render template current_date  formatdate 
#viet Get data.
#tao 1 class home. Truyen nhung bien nhu ftdate ctdate de ke thua.
#class home get.c'mon data. [get_context_data]
##get_context_data get view_teample 
#return html

###get_context_data:
###context['current_date']=hghghg

#models - urls match data - database cung ten.
