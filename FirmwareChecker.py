# -*- coding: UTF-8 -*-
import urllib2, urllib, json
import time
import sys

while True:
	firmare_url = "https://api.ipsw.me/v2.1/firmwares.json/"
	data = json.loads(urllib2.urlopen(firmare_url).read())
	devices = data["devices"]
	for device in devices:
		device_firmware = data["devices"][device]["firmwares"]
		ios_device_name = data["devices"][device]["name"]
		for firmware in device_firmware:
			#board_config = data["devices"][device]["BoardConfig"]
			ios_signed = firmware["signed"]
			ios_version = firmware["version"]
			ios_build = firmware["buildid"]
			previous_version = ios_version
			if ios_signed == True:
				print"%s iOS %s (%s)"  % (ios_device_name, ios_version, ios_build)	
	time.sleep(3600)
