
"""unit test for ActiveCalendar"""
import unittest
from unittest.mock import MagicMock, patch
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

        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(2023, 3, 6, 9, 0,tzinfo=pytz.utc)
            activeCalendar = ActiveCalendar(calendar)
        #check that no events are active at 9:00 AM
        self.assertEqual(activeCalendar.activeEvents,[])

        #move the clock to 10:30AM and update the active events:
        with patch('datetime.dateteime') as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(2023, 3, 6, 10, 30,tzinfo=pytz.utc)
            active, inactive, missed = activeCalendar.wake()

        #check that active, inactive, and missed are correct
        self.assertEqual(missed,[])
        self.assertEqual(inactive,[])
        self.assertEqual(len(active),1)
        self.assertEqual(active[0]['summary'],'Event 1')
        
        
        
