This is a python module for tracking when icalendar events become active/inactive.  
It uses `recurring_ical_events` in addition to `icalendar` to support calendars with recurring events.  
It maintains a list of events today that are not yet active, sorted by when they will become active,  
and a list of events today that are currently active, sorted by when they will become inactive.  
Every time the `wake` method is called, it will update both of these lists.  
It will also return a tuple `(newlyActive,newlyInactive,missed`)  
which are each lists of, respectively:  
* events that became active since `wake` was last called,
* events that were active at the time `wake` was last called, but are no-longer
* events that both became active and then became inactive since `wake` was last called.  

It also updates a field `nextTime` which stores the datetime for the soonest time that any event will become active or become inactive.  
The intended use is that this value be used to determine when to next call the method `wake`.  
This module is not yet well-tested,  
and it does not yet support tracking events over multiple days,  
only within the day it is started.  
This should hopefully be remedied soon?  

Sorry I haven't set up a license yet.  
I'm indecisive.  
For the time being, you have my permission to use this (with or without modifications) for your own personal-and-private use, provided that you agree/accept/etc. that I don't have or accept any liability for any flaws in this software (of which there are many), and that there is no warranty or implicit claim that this software isn't total garbage, etc. etc. standard disclaimer.  
In addition, for the time being, I grant permission to fork this project on Github and by doing so distribute modifed forms of it, *provided* that it is for the purpose of contributing to this project of mine.  
This permission does not include maintaining a fork which is meant to be a competitor or replacement to this project of mine.
However!: I anticipate granting a much more permissive license in the near future! I'm just putting these restrictive permissions out now, until I make a decision about what license I want to actually provide long-term.
If the current lack of a more permissive license is an impedement for something you would like to do, please let me know!
If you do, I will probably hurry up and actually choose a permissive license that will hopefully be suitable.  

In addition, even if you are not interested in contributing actual code to this, I would still be interested in any suggested improvements to it and/or my lack of providing a license for it.  

Feel free to contact me about this project.
