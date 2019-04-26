import validate_directory

FILE_FORMAT = ".mavi" #Custom file format
DATA_SEPARATOR = ";"

SONG_DIRECTORY = "songs/"

validate_directory.validate_directory(SONG_DIRECTORY)

def load_saved_song_data(song_file):
	SONG_TITLE_INDEX = 0
	COMPOSER_INDEX = 1
	DEFAULT_OCTAVE_INDEX = 2
	RTTTL_STRING_INDEX = 3

	reading_file = open(song_file, "r")
	song_data_split = reading_file.read().split(DATA_SEPARATOR)
	reading_file.close()
	
	song_title = song_data_split[SONG_TITLE_INDEX]
	composer = song_data_split[COMPOSER_INDEX]
	default_octave = song_data_split[DEFAULT_OCTAVE_INDEX]
	RTTTL_string = song_data_split[RTTTL_STRING_INDEX]
	
	return [song_title, composer, default_octave, RTTTL_string]

def save_song_to_file(song_title, composer, default_octave, RTTTL_string):
	writing_file = open(SONG_DIRECTORY + song_title + FILE_FORMAT, "w")
	writing_file.write(song_title + DATA_SEPARATOR + composer + DATA_SEPARATOR + default_octave + DATA_SEPARATOR + RTTTL_string)
	writing_file.close()