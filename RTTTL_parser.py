'''
Module Description: A simplified interface for interacting with the gTTS text-to-speech engine.
'''

def clense_RTTTL_string(RTTTL_string):
	return RTTTL_string.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", "").lower()
	
#A readable note buffer is a note buffer that has been formatted to be read out loud by the text-to-speech engine.
def parse_RTTTL_to_readable_note_buffer(song_title, composer, default_octave, RTTTL_string): 
	NOTE_DURATION_INDEX = 0
	
	READABLE_DOTTED_NOTE = "dotted"
	RTTTL_DOTTED_NOTE = "."
	
	READABLE_DOUBLE_DOTTED_NOTE = "double dotted"
	RTTTL_DOUBLE_DOTTED_NOTE = ".."
	
	READABLE_TRIPLE_DOTTED_NOTE = "tripple dotted"
	RTTTL_TRIPLE_DOTTED_NOTE = "..."
	
	READABLE_SHARP_NOTE = "sharp"
	RTTTL_SHARP_NOTE = "#"
	
	READABLE_REST = "rest"
	RTTTL_REST = "p"
	
	READABLE_DEFAULT_OCTAVE = "default octave"
		
	READING_PAUSE = ". . . " #a special string that dictates how the voice will pause between reading two different strings.
	
	readable_song_information = song_title + " by " + composer + READING_PAUSE + READABLE_DEFAULT_OCTAVE + default_octave + READING_PAUSE
	
	note_durations = {"1" : "whole note ", "2" : "half note ", "4" : "quarter note ", "8" : "eighth note ", "16" : "sixteenth note ", "32" : "thirty-second note "}
	sharp_note_values = {"c#" : "c sharp ", "d#" : "d sharp ", "e#" : "e sharp ", "f#" : "f sharp ", "g#" : "g sharp ", "a#" : "ayy sharp ", "b#" : "b sharp "} #'ayy' needed for correct pronounciation
	
	RTTTL_string = clense_RTTTL_string(RTTTL_string)
	RTTTL_note_buffer = RTTTL_string.split(",")
	
	readable_note_buffer = readable_song_information

	for note in RTTTL_note_buffer:
		note_value_index = 1
		if RTTTL_TRIPLE_DOTTED_NOTE in note:
			readable_note_duration = READABLE_TRIPLE_DOTTED_NOTE + " " + note_durations[note[NOTE_DURATION_INDEX]]
		elif RTTTL_DOUBLE_DOTTED_NOTE in note:
			readable_note_duration = READABLE_DOUBLE_DOTTED_NOTE + " " + note_durations[note[NOTE_DURATION_INDEX]]
		elif RTTTL_DOTTED_NOTE in note:
			readable_note_duration = READABLE_DOTTED_NOTE + " " + note_durations[note[NOTE_DURATION_INDEX]]
		else:
			try:
				int(note[NOTE_DURATION_INDEX+1])
				readable_note_duration = note_durations[note[NOTE_DURATION_INDEX] + note[NOTE_DURATION_INDEX + 1]] #Used to test for 16th and 32nd notes; without this, the parser interprets the "1" as a whole note.
				note_value_index += 1
			except:
				readable_note_duration = note_durations[note[NOTE_DURATION_INDEX]]
		
		if RTTTL_REST in note:
			readable_note_buffer += readable_note_duration + READING_PAUSE + READABLE_REST + READING_PAUSE
		else:
			if RTTTL_SHARP_NOTE in note:
				readable_note_value = sharp_note_values[note[note_value_index] + RTTTL_SHARP_NOTE]
			else:
				readable_note_value = note[note_value_index]
			try: 
				int(note[len(note)-1])
				readable_octave = "octave " + note[len(note)-1]
				readable_note_buffer += readable_note_duration + READING_PAUSE + readable_note_value + READING_PAUSE + readable_octave + READING_PAUSE
			except:
				readable_note_buffer += readable_note_duration + READING_PAUSE + readable_note_value + READING_PAUSE #For clarity sake, note duration is always read first for both notes and rests.
		
	return readable_note_buffer	