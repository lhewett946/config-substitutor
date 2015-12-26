# config-substitutor
The config_switcher.py script allows users to define a set of config changes that they would like to make. These changes are stored in the .overrides files, which use a JSON format as described below:
```json
{
	"<config file path>":
		[
	 		{"original": "<original text>","modified": "<modified text>"}
		]
}
```
Note that this script will only support modifications which can be applied using simple substitutions, there is no support for adding or removing lines completely (for example adding or removing items from Forestry backpacks).

Storing the config file changes in this format means that it is easy to tell when the default value for a config option is changed by the mod author, as the override will no longer be applied by the script. Any overrides which are not applied are printed to the console so the user can review and update them as required.

Currently there is no error checking on the JSON parsing, so an invalid JSON input will cause the script to crash. It is suggested that the JSON input is validated by an external tool (such as http://jsonlint.com/) before the script is used.

Usage : create the override files and run the script, providing the command line arguments for the directory containing the overrides and the directory containing the config files. By default the script will assume that both are in the same directory as the script. I suggest using one .overrides file per mod - although if you wish you could use a single file for all your mods!
