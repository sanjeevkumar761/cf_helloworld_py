"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import requests


def getData():
#	r = requests.get('https://preemeahana3aa2814455.hana.ondemand.com/SwissRE/swissredbservice/TRANS_FX.xsodata/TRANS_FX?$format=json')	
#	r.json()
	s = requests.Session()
	url= 'https://preemeahana3aa2814455.hana.ondemand.com/SwissRE/swissredbservice/TRANS_FX.xsodata/TRANS_FX?$format=json'
	auth= ('SRADMIN','London123')
#	s.headers= (name= 'content-type',
#	value= 'application/json'
#	)
s.get(url, auth=auth)                          

if __name__ == '__main__':
	getData()
	



