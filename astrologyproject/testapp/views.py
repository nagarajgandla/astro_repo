from django.shortcuts import render

# Create your views here.
import datetime, random


def results_view(request):
    time = datetime.datetime.now()
    names_list = ['Anushka', 'Deepika', 'Alia', 'Katrina']
    msg_list = [
        'The golden days ahead',
        'Tomorrow is the perfect day to start new things',
        'Very soon you will get job'
    ]
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'
    else:
        s = 'Good night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time': time, 'name': name, 'msg': msg, 'wish': s}
    return render(request, 'testapp/astrology.html', my_dict)