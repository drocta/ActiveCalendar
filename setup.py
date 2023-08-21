
from setuptools import setup, find_packages

setup(
        name="active_calendar",
        version="0.1",
        packages=find_packages(),
        install_requires=[
                'icalendar',
                'recurring_ical_events',
                'pytz'
            ]
        )
