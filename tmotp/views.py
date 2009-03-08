from django.http import HttpResponse
from tmotp.models import Card,Game,CardStatus
from django.shortcuts import render_to_response

def index(request):
    game, = Game.objects.all()
    
    unplayed = [s.card for s in CardStatus.objects.filter(game=game,status__available=True)]
    
    unplayed_cards = len( unplayed )
    unplayed_dem = len([x for x in unplayed if x.democrat and not x.republican])
    unplayed_gop = len([x for x in unplayed if x.republican and not x.democrat])
    deck_leans = unplayed_dem - unplayed_gop
    if deck_leans > 0:
        deck_leans_who = 'GOP'
    elif deck_leans < 0:
        deck_leans_who = 'Dem'
    else:
        deck_leans_who = 'Even'
        
    cards = [c for c in Card.objects.filter(cardstatus__status__name='Our Hand').order_by('title')]

    return render_to_response('hand.html',
    {'cards': cards,
     'unplayed_cards': unplayed_cards,
     'unplayed_dem': unplayed_dem,
     'unplayed_gop': unplayed_gop,
     'unplayed_both': len([x for x in unplayed if x.republican and x.democrat]),
     'deck_leans_amount': abs(deck_leans),
     'deck_leans_who': deck_leans_who,
     'remaining_cp': sum([c.campaign_points for c in unplayed]),
     'remaining_rest': sum([c.rest_cubes for c in unplayed]),
     'dem_count': len([c for c in cards if c.democrat]),
     'gop_count': len([c for c in cards if c.republican]),
     'cp_sum': sum([c.campaign_points for c in cards]),
     'rest_sum': sum([c.rest_cubes for c in cards]),
    }
    )