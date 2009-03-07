from django.db import models

class State(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.code
        
class Issue(models.Model):
    code = models.CharField(max_length=2, unique=True)
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
    
    def __unicode__(self):
        return self.title
