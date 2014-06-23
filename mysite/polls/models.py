from django.db import models
import datetime
from django.utils import timezone

# Create 2 classes Poll and Choice
# Create Poll class
class Poll(models.Model):
    question = models.CharField(max_length=200) #Question is a string with max length = 200 characters
    pub_date = models.DateTimeField('date published') #Date published of poll's question
    #Function return the question of poll
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field ='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description ='Published recently?'

# Create Choice class
class Choice(models.Model):
    poll = models.ForeignKey(Poll) #'cause each choice associated with a Poll
    choice_text = models.CharField(max_length=200) #choice text is a string with max length = 200 char
    votes = models.IntegerField(default=0) #vote tally of the choice, default is 0
    #Function return choice
    def __unicode__(self):
        return self.choice_text
