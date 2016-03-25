from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "Room id: {0}".format(self.id)

class Character(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room)

    def moove(self, portal): #TODO: direction
        if not portal.is_enable:
            print("Portal is not enable")
        else:
            if portal.entry == self.room:
                self.room = portal.exit
                print("Character has been mooved")
            else:
                print("Player has no access to portal entry")

    def __unicode__(self):
        "Character id: {0}".format(self.id)

class Portal(models.Model):
    is_enable = models.BooleanField(default=True)
    direction = models.CharField(max_length=1)
    entry = models.ForeignKey(Room, related_name='portal_entry')
    exit = models.ForeignKey(Room, related_name='portal_exit')

    def __unicode__(self):
        "Portal id: {0}".format(self.id)