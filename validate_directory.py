import os

def validate_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)