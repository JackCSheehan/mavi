'''
Module Description: A simplified interface for interacting with the gTTS text-to-speech engine.
'''
from gtts import gTTS
import RTTTL_parser
import validate_directory

LANGUAGE = "en"
AUDIO_FOLDER_PATH = "audio/"
FILE_FORMAT = ".mp3"

validate_directory.validate_directory(AUDIO_FOLDER_PATH)

def save_to_mp3(song_title, composer, default_octave, RTTTL_string):
	RTTTL_as_readable_string = RTTTL_parser.parse_RTTTL_to_readable_note_buffer(song_title, composer, default_octave, RTTTL_string)
	
	text_to_speech = gTTS(text = RTTTL_as_readable_string, lang = LANGUAGE)
	text_to_speech.save(AUDIO_FOLDER_PATH + song_title + FILE_FORMAT)



