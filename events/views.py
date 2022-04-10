from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


def home(request, year, month):
    name = "Timz Owen"
    month_number = list(calendar.month_name).index(month)
    return render(request, "home.html", {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
    })
