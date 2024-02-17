from django.shortcuts import render


def itunes_gift_cards(request):
    return render(request, 'itunes_gift_cards.html')
