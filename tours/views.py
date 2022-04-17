from random import sample
from django.shortcuts import render
from django.template.defaultfilters import lower

from tours import data

# Create your views here.
def main_view(request):
    itog = {}
    x = range(1, len(data.tours))
    x = sample(x, 6)
    count = 0
    for i in x:
        itog[i] = data.tours[i]

    context = {
        'x': x,
        'tour_id': itog,
        'tours': data.tours,
        'subtitle': data.subtitle,
        'description': data.description,
        'departur': data.departures,
        'title': data.title,
    }
    return render(request, 'tours/index.html', context=context, )


def departure_view(request, departure):


    spisok_tour = {}
    price = []
    nights = []
    count = 0
    for key, value in data.tours.items():
        if value['departure'] == departure:
            spisok_tour[key] = value
            price.append(value['price'])
            nights.append(value['nights'])
            count += 1
    min_price = min(price)
    max_price = max(price)
    min_nights = min(nights)
    max_nights = max(nights)

    context = {
        'tours': spisok_tour,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures[departure],
        'departur': data.departures,
        'title': data.title,
        'departure': departure,
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
        'price': price,
        'nights': nights,
        'count': count,

    }
    return render(request, 'tours/departure.html', context=context, )


def tour_view(request, tour_id):
    zvezda = int(data.tours[tour_id]['stars']) * '★'
    country_from = data.departures[data.tours[tour_id]['departure']]
    country_to = data.tours[tour_id]['country']
    nights = data.tours[tour_id]['nights']
    from_to = (country_to + " " + (country_from) + " на " + str(nights) + " ночей")

    context = {
        'tours': data.tours,
        'subtitle': data.subtitle,
        'description': data.description,
        'title': data.title,
        'tour_id': tour_id,
        'zvezda': zvezda,
        'from_to': from_to,
        'departur': data.departures,
    }
    return render(request, 'tours/tour.html', context=context, )
