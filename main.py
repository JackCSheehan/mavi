'''
Module Discription: All of the UI for this music software is defined/initalized in this file.
'''
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import text_to_speech_engine
import song_parser
import RTTTL_parser

def quit():
	sys.exit(0)

root = Tk()

DEFAULT_WINDOW_WIDTH = 820
DEFAULT_WINDOW_HEIGHT = 630

WINDOW_TITLE = "MAVI 2019"

root.geometry(str(DEFAULT_WINDOW_WIDTH) + "x" + str(DEFAULT_WINDOW_HEIGHT))
root.title(WINDOW_TITLE)

Y_PADDING = 8
X_PADDING = 5

BUTTON_FONT = ("Arial", 11)
LABEL_FONT = ("Arial", 11)
HEADER_FONT = ("Arial", 18, "bold")
ENTRY_FONT = ("Arial", 10)

note_entry_menu = Frame(root)
main_menu = Frame(root)

def display_main_menu():
	note_entry_menu.pack_forget()
	main_menu.pack()

def display_note_entry_menu():
	main_menu.pack_forget()
	note_entry_menu.pack()
	
#Main menu defintions
main_menu_title = Label(main_menu, text = "Musical Assistance for the Visually Impaired\nMAVI", font = HEADER_FONT)
main_menu_title.pack(pady = Y_PADDING)

enter_note_entry_mode_button = Button(main_menu, text = "Note Entry Mode", font = BUTTON_FONT, command = display_note_entry_menu)
enter_note_entry_mode_button.pack(pady = Y_PADDING)

information_button = Button(main_menu, text = "Information", font = BUTTON_FONT, command = lambda:messagebox.showinfo("Information", """(c) 2019 Jack Sheehan\n\nDeveloped Using:\nPython 3.6\nTkinter 8.6\nRTTTL (wikipedia.org/wiki/Ring_Tone_Transfer_Language)\ngTTS 2.0.3 (github.com/pndurette/gTTS)\n\nSource located at: github.com/CodeTimesTen\n
gTTS License:

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
"""))
information_button.pack()

exit_button = Button(main_menu, text = "Exit", font = BUTTON_FONT, command = quit)
exit_button.pack(pady = Y_PADDING)

copyright = Label(main_menu, text = "Copyright (c) 2019 Jack Sheehan")
copyright.pack(pady = Y_PADDING, side = BOTTOM)
	
#Note entry mode definitions

note_entry_header = Label(note_entry_menu, text = "Note Entry Interface", font = HEADER_FONT)
note_entry_header.pack(pady = Y_PADDING)

song_title_label = Label(note_entry_menu, text = "Song Title:", font = LABEL_FONT)
song_title_label.pack()
song_title_entry = Entry(note_entry_menu, font = ENTRY_FONT)
song_title_entry.pack()

composer_label = Label(note_entry_menu, text = "Composer:", font = LABEL_FONT)
composer_label.pack()
composer_entry = Entry(note_entry_menu, font = ENTRY_FONT)
composer_entry.pack()

default_octave_label = Label(note_entry_menu, text = "Default Octave:", font = LABEL_FONT)
default_octave_label.pack()
default_octave_entry = Entry(note_entry_menu, font = ENTRY_FONT)
default_octave_entry.pack()

RTTTL_editor_title = Label(note_entry_menu, text = "Edit RTTTL Data Below:", font = LABEL_FONT)
RTTTL_editor_title.pack(pady = Y_PADDING)

NUMBER_OF_EDITOR_LINES = 12

RTTTL_editor = Text(note_entry_menu, height = NUMBER_OF_EDITOR_LINES, font = ENTRY_FONT)
RTTTL_editor.pack(pady = Y_PADDING)

def clear_all_fields(ask_user_to_confirm):
	if ask_user_to_confirm:
		if messagebox.askquestion("New Song", "Are you sure you want to start a new song? Any unsaved progress will be lost.", icon = "question") == "no":
			return

	song_title_entry.delete(0, END)
	composer_entry.delete(0, END)
	default_octave_entry.delete(0, END)
	RTTTL_editor.delete("1.0", END)

new_song_button = Button(note_entry_menu, text = "New Song", font = BUTTON_FONT, command = lambda:clear_all_fields(True))
new_song_button.pack(pady = Y_PADDING)

def load_song():
	LOADED_SONG_TITLE_INDEX = 0
	LOADED_COMPOSER_INDEX = 1
	LOADED_DEFAULT_OCTAVE_INDEX = 2
	LOADED_RTTTL_STRING_INDEX = 3
	
	loaded_song_data = song_parser.load_saved_song_data(filedialog.askopenfilename())
	
	clear_all_fields(False)
	
	song_title_entry.insert(0, loaded_song_data[LOADED_SONG_TITLE_INDEX])
	composer_entry.insert(0, loaded_song_data[LOADED_COMPOSER_INDEX])
	default_octave_entry.insert(0, loaded_song_data[LOADED_DEFAULT_OCTAVE_INDEX])
	RTTTL_editor.insert("1.0", loaded_song_data[LOADED_RTTTL_STRING_INDEX])

load_song_button = Button(note_entry_menu, text = "Load Song", command = load_song, font = BUTTON_FONT)
load_song_button.pack(pady = Y_PADDING)

def save_and_export():
	FORBIDDEN_CHARACTERS = ["<", ">", ":", "/", "\\", "|", "?", "*", "\""]
	try:
		try:
			int(default_octave_entry.get())
		except:
			messagebox.showerror("Error", "The default octave must be an integer value.")
		clensed_RTTTL_string = RTTTL_parser.clense_RTTTL_string(RTTTL_editor.get("1.0", "end-1c"))
		MAX_CHARACTERS_IN_TITLE = 40
		if len(song_title_entry.get()) > MAX_CHARACTERS_IN_TITLE:
			messagebox.showerror("Error", "Song titles cannot be longer than " + str(MAX_CHARACTERS_IN_TITLE) + "characters")
		elif clensed_RTTTL_string == "" or song_title_entry.get() == "" or composer_entry.get() == "" or default_octave_entry.get() == "":
			messagebox.showerror("Error", "You cannot leave any of the fields blank. Please fill them in before trying to save and export.")
		elif any(i in song_title_entry.get() for i in FORBIDDEN_CHARACTERS):
			messagebox.showerror("Error", "The tite of your song contains forbidden directory characters. Please change your title so that it does not contain any of the following characters: " + str(FORBIDDEN_CHARACTERS))
		else:
			root.title("Loading...")
			song_parser.save_song_to_file(song_title_entry.get(), composer_entry.get(), default_octave_entry.get(), clensed_RTTTL_string)
			text_to_speech_engine.save_to_mp3(song_title_entry.get(), composer_entry.get(), default_octave_entry.get(), clensed_RTTTL_string)
			root.title(WINDOW_TITLE)
	except:
		messagebox.showerror("Error", "Something has gone wrong while trying to convert your song. Please chcek your RTTTL data and dry again.") #A catch-case for any unplannable exceptions that arise from an RTTTL mistake

save_and_export_button = Button(note_entry_menu, text = "Save and Export as MP3", font = BUTTON_FONT, command = save_and_export)
save_and_export_button.pack(pady = Y_PADDING)

exit_to_main_menu_button = Button(note_entry_menu, text = "Exit to Main Menu", font = BUTTON_FONT, command = display_main_menu)
exit_to_main_menu_button.pack(pady = Y_PADDING)

display_main_menu()#default menu

root.update()
root.mainloop()
