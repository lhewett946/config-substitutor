# minecraft-configs
The config_switcher.py script allows users to define a set of config changes that they would like to make. These changes are stored in the .overrides files, which use a JSON format as described below:

{
	"<config file path>":
		[
	 		{"original": "<original text>","modified": "<modified text>"}
		]
}

Note that this script will only support modifications which can be applied using simple substitutions, there is no support for adding or removing lines completely (for example adding or removing items from Forestry backpacks).

Storing the config file changes in this format means that it is easy to tell when the default value for a config option is changed by the mod author, as the override will no longer be applied by the script. Any overrides which are not applied are printed to the console so the user can review and update them as required.

Currently there is no error checking on the JSON parsing, so an invalid JSON input will cause the script to crash. It is suggested that the JSON input is validated by an external tool (such as http://jsonlint.com/) before the script is used.

Usage : add the override files into the Minecraft instance's config directory and run the script from there. I suggest using one .overrides file per mod - although if you wish you could use a single file for all your mods!