#!/usr/bin/python

import os
import json

## load json file to a Python dictionary
def load_json(filename):
	f = open(filename,'r')
	overrides = json.load(f)
	return overrides

## perform the replacements
def replace_lines(file, overrides):
	if os.path.isfile(file):
		config_file = open(file,'r')
		file_lines = config_file.readlines()
		config_file.close()		

		# iterate through the overrides
		for override in overrides:
			file_lines_modified = []
			# flag when an override succeeds
			override_succeeded = False
			# check each line to see if the override can be applied
			for line in file_lines:
				new_line = line
				new_line = new_line.replace(override["original"],override["modified"])
				if line != new_line:
					override_succeeded = True
				file_lines_modified.append(new_line)

			# update local copy of config file with modified lines
			file_lines = file_lines_modified
			
			# print any overrides which could not be applied
			if override_succeeded is False:
				print(file + ": Unable to override " + override["original"] + " with " + override["modified"])

		# write out modified file
		config_file = open(file, 'w')
		config_file.writelines(file_lines)
		config_file.close()
	else:
		print(file + " does not exist")

# find all overrides in the directory
for file in os.listdir("."):
	if file.endswith(".overrides"):
		overrides = load_json(file)

		for config_filename in overrides:
			option_overrides = overrides[config_filename]
			replace_lines(config_filename, option_overrides)

print ("Finished overriding config options")