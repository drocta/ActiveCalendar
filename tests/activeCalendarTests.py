
"""unit test for ActiveCalendar"""
import unittest
import time_machine
from activeCalendar import ActiveCalendar
import icalendar
import datetime
import pytz

testFileLocation = r'./example.ics'#r'./testCalendar1.ics'

def calFromFile(filepath):
    with open(filepath,'r') as f:
        ical_string = f.read()
        calendar = icalendar.Calendar.from_ical(ical_string)
        return calendar

def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()

class TestActiveCalendar(unittest.TestCase):
    def test_active_events(self):
        calendar = calFromFile(testFileLocation)

        with time_machine.travel(datetime.datetime(2023, 3, 6, 9, 0,tzinfo=pytz.utc),tick=False):
            activeCalendar = ActiveCalendar(calendar)
        #check that no events are active at 9:00 AM
        self.assertEqual(activeCalendar.activeEvents,[])

        #move the clock to 10:30AM and update the active events:
        with time_machine.travel(datetime.datetime(2023, 3, 6, 10, 30,tzinfo=pytz.utc),tick=False):
            active, newlyInactive, missed = activeCalendar.wake()

        #check that active, inactive, and missed are correct
        self.assertEqual(missed,[])
        self.assertEqual(newlyInactive,[])
        self.assertEqual(len(active),1)
        self.assertEqual(active[0]['summary'],'Event 1')

        # Move the clock to 11:30 AM and update the active events
        with time_machine.travel(datetime.datetime(2023, 3, 6, 11, 30,tzinfo=pytz.utc),tick=False):
            active, newlyInactive, missed = activeCalendar.wake()
        self.assertEqual(missed, [])
        self.assertEqual(active, [])
        self.assertEqual(len(newlyInactive),1)
        self.assertEqual(newlyInactive[0]['summary'], 'Event 1')
        
        # Move the clock to 2:00 PM and update the active events
        with time_machine.travel(datetime.datetime(2023, 3, 6, 14, 0,tzinfo=pytz.utc),tick=False):
            active, newlyInactive, missed = activeCalendar.wake()
        self.assertEqual(missed, [])
        self.assertEqual(newlyInactive, [])
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0]['summary'], 'Event 2')
        
