# mavi
Musical Assistance for the Visually Impaired (MAVI) is an open source program that aids visually impaired musicians in learning their music.

MAVI is programmed in Python 3.6 and takes advantage of both Tkinter and the gTTS library (https://github.com/pndurette/gTTS). 

Songs are stored in RTTTL format. RTTTL is a music language created by Nokia. For more info, visit: https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language

MAVI provides the user with input areas for RTTTL code that are then parsed, converted to speech using the gTTS library, and downloaded as an MP3. The text-to-speech voice reads out notes, note lengths, and note octaves so that visually impaired musicians gain a basic technical understanding of a specific piece of music.

# Technical Challenges/What I Learned
* Parsed RTTTL code into a format that can be more easily read by text-to-speech
* Practiced Python Tkinter GUI creation
* Learned how to use the gTTS library in Python
