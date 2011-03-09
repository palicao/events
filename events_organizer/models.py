from django.db import models
from django.contrib.auth.models import User
from time import strftime
from datetime import datetime

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = u"Countries"


class City(models.Model):
	name = models.CharField(max_length=200)
	country = models.ForeignKey(Country)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name_plural = u"Cities"
	
	
class Event(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	city = models.ForeignKey(City)
	dateStart = models.DateField(null=True, blank=True)
	timeStart = models.TimeField(null=True, blank=True)
	dateEnd = models.DateField(null=True, blank=True)
	timeEnd = models.TimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.name


class EventOption(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	
	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	city = models.ForeignKey(City)
	phone_number = models.CharField(max_length=20, null=True, blank=True) # todo PhoneNumberField ?
	fax_number   = models.CharField(max_length=20, null=True, blank=True) # todo PhoneNumberField ?
	
	def __unicode__(self):
		return self.user.username # ???
		
	
class Invite(models.Model):
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User) # ???
	
	def __unicode__(self):
		return u'Invito per ' + self.event.name
	
	
class InviteLog(models.Model):
	invite = models.ForeignKey(Invite)
	recipient = models.ForeignKey(User)
	sent = models.DateTimeField(default=datetime.now) # NOW
	
	def __unicode__(self):
		return u'Invito per ' + self.invite.event.name + ' inviato il ' + \
		       self.sent.strftime("%s %s" % ("%Y-%m-%d", "%H:%M:%S"))


class Reservation(models.Model):
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User)
	accepted = models.DateTimeField(default=datetime.now) # NOW
	
	def __unicode__(self):
		return u'Prenotazione per ' + self.event.name + u' da ' + self.user.username
	
class ReservationOption(models.Model):
	reservation = models.ForeignKey(Reservation)
	choosen_option = models.ForeignKey(EventOption)
	
	def __unicode__(self):
		return u'Opzione presa per l\'evento ' + self.reservation.event.name + \
		       ' da ' + self.reservation.user.username + ' su ' + \
		       self.choosen_option.name