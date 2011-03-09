from events_organizer.models import Country, City, Event, EventOption
from events_organizer.models import UserProfile, Invite, InviteLog
from events_organizer.models import Reservation, ReservationOption
from django.contrib import admin

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(EventOption)
admin.site.register(UserProfile)
admin.site.register(Invite)
admin.site.register(InviteLog)
admin.site.register(Reservation)
admin.site.register(ReservationOption)
