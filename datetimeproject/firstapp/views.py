from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetime_info(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Welcome Very'
    h=int(date.strftime('%H'))
    if h<12:
        msg=msg+'Good Morning'
    elif h<16:
        msg=msg+'Good Afternoon'
    elif h<21:
        msg=msg+'Good Evening'
    else:
        msg=msg+'Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1>Now Server time is :'+str(date)+'</h1>'
    return HttpResponse(msg)
