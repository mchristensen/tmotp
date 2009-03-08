from django.db import models

class State(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.code
        
class Issue(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.code
        
class Card(models.Model):
    title = models.CharField(max_length=255)
    campaign_points = models.PositiveIntegerField(default=0)
    rest_cubes = models.PositiveIntegerField(default=0)
    
    democrat = models.BooleanField()
    republican = models.BooleanField()
    
    state = models.ForeignKey(State, blank=True,null=True)
    issue = models.ForeignKey(Issue, blank=True,null=True)

    event_text = models.TextField()
    
    def party(self):
        if self.democrat and self.republican:
            return 'Both'
        elif self.democrat:
            return 'D'
        else:
            return 'R'
    
    def __unicode__(self):
        return self.title
        
class Status(models.Model):
    name = models.CharField(max_length=30,unique=True)    
    in_hand = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Game(models.Model): 
    name = models.CharField(max_length=30,unique=True)
    
    def initialize(self):
        for card in Card.objects.all():
            try:
                CardStatus.objects.get(card=card, game=self)
            except:           CardStatus.objects.create(card=card,game=self,status=Status.objects.get(name='Deck'))
    
    def __unicode__(self):
        return self.name
        
class CardStatus(models.Model):
    card = models.ForeignKey(Card)
    status = models.ForeignKey(Status)
    game = models.ForeignKey(Game)
    
    def card_party(self):
        return self.card.party()
            
    def card_title(self):
        return self.card.title

    def card_campaign_points(self):
        return self.card.campaign_points
        
    def card_rest_cubes(self):
        return self.card.rest_cubes

    def card_issue(self):
        return self.card.issue

    def card_state(self):
        return self.card.state
        
    def card_event_text(self):
        return self.card.event_text
    
    def __unicode__(self):
        return u'%s, %s' % (self.card,  self.status)
