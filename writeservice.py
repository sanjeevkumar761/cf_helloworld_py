from flask import Flask, request
from flask_restful import Resource, Api
import os
from quickstart import getData
import json

# from restapi import TodoSimple


app = Flask(__name__)
api = Api(app)

port = int(os.getenv("PORT", 9009))



todos = {
    '1':  'My first task.',
    '2':  'Remeber the milk.'
}
	
class DataWriter(Resource):
	def put(self):
#		f1 = request.form['data']
		f1 = request.form['BusinessTransActionID']
		f2 = request.form['SourceSystem']
		f3 = request.form['PostingDate']
		f4 = request.form['Account']
		f5 = request.form['ExternalContract']
		f6 = request.form['TransactionAmount']

		print (f1,f2,f3,f4,f5,f6)





		#specify url
		url = 'my URL'

		token = "my token"
		data = request.form

		headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", data:data}

		#Call REST API
		#response = requests.put(url, data=data, headers=headers)

		#Print Response
		#print(response.text)



		tmpStr = '{"uri": "https://preemeahana3aa2814455.hana.ondemand.com/SwissRE/swissredbservice/TRANS_FX.xsodata/TRANS_FX","headers": [ { "name": "content-type", "value": "application/json" } ],                          "method": "POST", "auth": { "user": "SRADMIN", "pass": "London123", "sendImmediately": true },"json": { "ACCOUNT" : "CASH", "BUSINESSTRANSACTIONID" : "123", "EXTERNALCONTRACT" : "ACOUNT02", "FX_RATE" : "null", "POSTINGDATE" : "/Date(1525651200000)/", "SOURCESYSTEM" : "SRS", "TRANSACTIONAMOUNT" : "100", "TRANSACTION_CURR_ISO" : "CHF", "TRANSLATEDAMOUNT" : " ", "TRANSLATED_CURR_ISO" : "" } }'
		options = json.loads(tmpStr)
		print (options)








		return "OK"

	def post(self):
		return self.put()

	def get(self):
		print ("get ok")
		return {"OK"}


		

api.add_resource(DataWriter, '/write')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
