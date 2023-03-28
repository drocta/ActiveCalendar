
"""
This file is for keeping track of what events from a an icalendar calendar
are currently active.


"""

import datetime
import icalendar
import recurring_ical_events



class ActiveCalendar:
    def __init__(self, cal):
        """
        self.activeEvents : list of events active at last wake (or at init) sorted by DTEND.
        self.unfCal : unfoldable calendar

        Does not currently handle boundaries between days correctly,
        along with many other deficiencies 
        """
        self.cal = cal
        self.unfCal = recurring_ical_events.of(self.cal)
        self.today = datetime.date.today()
        events = self.unfCal.at(self.today)
        self.n = len(events)
        self.eventsByStart = events.copy()
        self.eventsByStart.sort(key=lambda ev:ev["DTSTART"].dt)
        self.eventsByEnd = events
        self.eventsByEnd.sort(key=lambda ev:ev["DTEND"].dt)
        self.now = datetime.datetime.now()
        self.activeEvents = []
        for i,ev in enumerate(self.eventsByStart):
            startDT = ev["DTSTART"].dt
            if(self.now < startDT):
                self.nextStartTime = startDT
                self.nextStartIndex = i
                break
            elif(self.now < ev["DTEND"].dt):
                self.eventsActive.append(ev)
            pass
        for i,ev in enumerate(self.eventsByEnd):
            endDT = ev["DTEND"].dt
            if(self.now < endDT):
                self.nextEndTime = endDT
                self.nextEndIndex = i
                break
            pass
        self.eventsActive.sort(key=lambda ev:ev["DTEND"].dt)
        self.nextTime = min(self.nextStartTime, self.nextEndTime)
        #maybe should use a priority queue to store the events to start and end?
        #self.eventsByEnd and self.nextEndIndex are probably unnecessary,
        #  as only need to loop through the events marked as active.

    def wake(self):
        """call this to update the current active list"""
        then = self.now
        now = datetime.datetime.now()
        newlyActive = []
        #newlyInactive = []
        missed = []
        
        for i in range(self.nextStartIndex,n):
            ev = self.eventsByStart[i]
            startDT = ev["DTSTART"].dt
            if(startDT <= now):
                if(now <= ev["DTEND"].dt):
                    newlyActive.append(ev)
                else:
                    missed.append(ev)
            else:
                self.nextStartTime = startDT
                self.nextStartIndex = i
                break
        m = len(self.activeEvents)
        for i in range(m):
            ev = self.activeEvents[i]
            endDT = ev["ENDDT"].dt
            if(now < endDT):
                newlyInactive = self.activeEvents[0:i]
                remaining = self.activeEvents[i:]
                break
        else: # meaning, if there was no break
            #so, all of the end dates in the activeEvents list are in the past
            newlyInactive = self.activeEventsList
            remaining = []
        self.activeEvents = remaining + newlyActive
        self.activeEvents.sort(key = lambda ev:ev["DTEND"].dt)
        self.now = now
        return (newlyActive,newlyInactive,missed)
        

