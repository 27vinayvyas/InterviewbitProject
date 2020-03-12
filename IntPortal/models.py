from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class Interview(models.Model):
    participant = models.ForeignKey(Participant, related_name='participants',on_delete=models.PROTECT)
    date_Start = models.DateTimeField()
    date_End = models.DateTimeField()

    def __str__(self):
        return self.participant.name
