#from __future__ import print_function
import urllib, time
from Adafruit_Thermal import *
from xml.dom.minidom import parseString
import  evernote.edam.type.ttypes       as Types
import  evernote.edam.notestore.ttypes  as NoteStoreTypes
from evernote.api.client import EvernoteClient 
import evernote.edam.notestore.NoteStore as NoteStore


dev_token = "S=s1:U=9210c:E=15a0bd38ada:C=152b4225d28:P=1cd:A=en-devtoken:V=2:H=225ba56475ba405f154924f29856bde2"


client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
 
noteStore = client.get_note_store()

filter = NoteStore.NoteFilter()
searchTerm = 'ryder'

filter.words= searchTerm
filter.ascending = False

spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True

ourNoteList = noteStore.findNotesMetadata(dev_token, filter, 0, 100, spec)

for note in ourNoteList.notes:
    print "%s :: %s" % (note.guid, note.title)

wholeNotes = []
for note in ourNoteList.notes:
    #wholeNote = noteStore.getNote(dev_token, note.guid, True) 
    wholeNote = noteStore.getNote(dev_token, note.guid, True,  False, False, False)
    
    print "Content length: %d" % wholeNote.contentLength
    wholeNotes.append(wholeNote)
    print "Title: %s " % wholeNote.title
    print "Note Conetent: %s " % wholeNote.content

    noteText = noteStore.getNoteSearchText(dev_token, note.guid, True, False)
    print "Note Contents are : %s"  % noteText

    noteInformation = noteStore.getNoteContent(dev_token, note.guid)
    print "Other method returns ... %s " % noteInformation
 




    WOEID = '2459115'

# Dumps one forecast line to the printer
def forecast(idx):
	tag     = 'yweather:forecast'
	day     = dom.getElementsByTagName(tag)[idx].getAttribute('day')
	lo      = dom.getElementsByTagName(tag)[idx].getAttribute('low')
	hi      = dom.getElementsByTagName(tag)[idx].getAttribute('high')
	cond    = dom.getElementsByTagName(tag)[idx].getAttribute('text')
	printer.print(day + ': low ' + lo )
	printer.print(deg)
	printer.print(' high ' + hi)
	printer.print(deg)
	printer.println(' ' + cond)

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
deg     = chr(0xf8) # Degree symbol on thermal printer

# Fetch forecast data from Yahoo!, parse resulting XML
dom = parseString(urllib.urlopen(
        'http://weather.yahooapis.com/forecastrss?w=' + WOEID).read())

# Print heading
printer.inverseOn()
printer.print('{:^32}'.format(
  dom.getElementsByTagName('description')[0].firstChild.data))
printer.inverseOff()

# Print current conditions
printer.boldOn()
printer.print('{:^32}'.format('Current conditions:'))
printer.boldOff()
printer.print('{:^32}'.format(
  dom.getElementsByTagName('pubDate')[0].firstChild.data))
temp = dom.getElementsByTagName('yweather:condition')[0].getAttribute('temp')
cond = dom.getElementsByTagName('yweather:condition')[0].getAttribute('text')
printer.print(temp)
printer.print(deg)
printer.println(' ' + cond)
printer.boldOn()

# Print forecast
printer.print('{:^32}'.format('Forecast:'))
printer.boldOff()
forecast(0)
forecast(1)





printer.print(noteText)
printer.feed(3)
