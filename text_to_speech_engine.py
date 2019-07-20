'''
Module Description: A simplified interface for interacting with the gTTS text-to-speech engine.

gTTS license:

The MIT License (MIT)

Copyright © 2014-2018 Pierre Nicolas Durette

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
