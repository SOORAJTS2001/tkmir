#this page is used to add custom tags to the template
#https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/
#https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/#django.template.Library
#https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/#django.template.Library.filter
#https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/#django.template.Library.simple_tag
#
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def days_until(date):
    print(datetime.now().time().minute)
    print(datetime.time(date).minute)
    minute = datetime.now().time().minute - datetime.time(date).minute #this is the difference in minutes
    hour = datetime.now().time().hour - datetime.time(date).hour#this is the difference in hours
    day = datetime.now().date() - datetime.date(date)#this is the difference in days
    if day.days == 0:#if the difference is less than a day
        if hour == 0:
            if minute == 0:
                return 'now'
            else:
                return str(minute) + ' minutes ago'
        else:
            return str(hour) + ' hours ago'
    return str(day.days) + ' days ago'